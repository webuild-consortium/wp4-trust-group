"""JAdES Compact Baseline B signing for LoTL JSON."""

import base64
import json
import time
from pathlib import Path
from typing import Any, Union

from jwcrypto import jwk, jws
from jwcrypto.common import json_encode

from tools.lotl.log import get_logger

logger = get_logger(__name__)


def _load_pem(data: Union[bytes, str, Path]) -> bytes:
    """Load PEM from path or return bytes."""
    if isinstance(data, Path):
        return data.read_bytes()
    if isinstance(data, str) and not data.strip().startswith("-----"):
        return Path(data).read_bytes()
    if isinstance(data, str):
        return data.encode("utf-8")
    return data


def _cert_to_b64(cert_pem: Union[bytes, str]) -> str:
    """Convert PEM certificate to base64 for x5c header."""
    from cryptography import x509
    from cryptography.hazmat.primitives import serialization

    if isinstance(cert_pem, str):
        cert_pem = cert_pem.encode("utf-8")
    cert = x509.load_pem_x509_certificate(cert_pem)
    der = cert.public_bytes(serialization.Encoding.DER)
    return base64.b64encode(der).decode("ascii")


def sign_json(
    payload: dict[str, Any],
    key_pem: Union[bytes, str, Path],
    cert_pem: Union[bytes, str, Path],
    algorithm: str = "RS256",
) -> dict[str, Any]:
    """Sign JSON payload with JAdES Compact Baseline B.

    Adds a ``signature`` key to the payload with the JWS JSON Serialization
    structure (RFC 7515 §7.2.2):

        payload["signature"] = {
            "protected": "<BASE64URL(UTF8(JWS Protected Header))>",  # str
            "signature": "<BASE64URL(JWS Signature)>",               # str
        }

    The protected header contains ``alg`` (algorithm), ``x5c`` (signing
    certificate chain, DER base64), and ``iat`` (Unix integer timestamp,
    mandatory from 2025-07-15 per TS 119 182-1 §5.1.11 / Table 1 note a).

    Args:
        payload: Unsigned JSON-serializable dict (will be modified in-place copy).
        key_pem: Private key in PEM format.
        cert_pem: Signing certificate in PEM format.
        algorithm: JWS algorithm (RS256, ES256, PS256).

    Returns:
        Payload dict with ``signature`` key added.
    """
    key_data = _load_pem(key_pem)
    cert_data = _load_pem(cert_pem)

    key = jwk.JWK.from_pem(key_data)
    cert_b64 = _cert_to_b64(cert_data)

    # Remove existing signature if present
    payload = dict(payload)
    payload.pop("signature", None)

    header = {
        "alg": algorithm,
        "x5c": [cert_b64],
        # TS 119 182-1 §5.1.11 / Table 1 note (a): iat mandatory from 2025-07-15; replaces sigT
        "iat": int(time.time()),
    }

    jws_token = jws.JWS(json_encode(payload))
    jws_token.add_signature(key, None, json_encode(header), None)

    compact = jws_token.serialize(compact=True)
    parts = compact.split(".")

    # RFC 7515 §7.2.2: "protected" = BASE64URL(UTF8(JWS Protected Header)) — the string, not the dict.
    # Signature covers ASCII(parts[0] || "." || parts[1]); storing the raw dict and re-encoding
    # during verify would change key order and break §5.2 step 8 validation.
    payload["signature"] = {
        "protected": parts[0],
        "signature": parts[2],
    }

    return payload


def verify_json(payload: dict[str, Any]) -> dict[str, Any]:
    """Verify JAdES signature on JSON payload.

    Args:
        payload: Signed payload with 'signature' key.

    Returns:
        Verified payload (without signature).

    Raises:
        ValueError: If signature is invalid or missing.
    """
    sig = payload.get("signature")
    if not sig:
        raise ValueError("No signature in payload")

    protected_b64 = sig.get("protected")
    sig_b64 = sig.get("signature")

    # protected must be the base64url string stored by sign_json (RFC 7515 §7.2.2)
    if not isinstance(protected_b64, str) or not sig_b64:
        raise ValueError("Invalid JAdES signature structure")

    # Decode once to extract x5c for key loading — do NOT re-encode for the compact token
    try:
        padding = (4 - len(protected_b64) % 4) % 4
        protected = json.loads(base64.urlsafe_b64decode(protected_b64 + "=" * padding))
    except Exception as exc:
        raise ValueError(f"Invalid JAdES signature structure: cannot decode protected header: {exc}") from exc
    if not isinstance(protected, dict):
        raise ValueError("Invalid JAdES signature structure: protected header is not a JSON object")

    x5c = protected.get("x5c") or sig.get("header", {}).get("x5c")
    if not x5c:
        raise ValueError("Invalid JAdES signature structure")

    cert_b64 = x5c[0] if isinstance(x5c, list) else x5c
    cert_der = base64.b64decode(cert_b64)
    from cryptography import x509
    from cryptography.hazmat.primitives import serialization

    cert = x509.load_der_x509_certificate(cert_der)
    cert_pem = cert.public_bytes(serialization.Encoding.PEM)
    key = jwk.JWK.from_pem(cert_pem)

    payload_copy = dict(payload)
    payload_copy.pop("signature", None)

    def b64url_encode(data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode().rstrip("=")

    # Rebuild JWS compact using the original protected_b64 — must not re-encode the dict
    # (RFC 7515 §5.2 step 8: signature covers ASCII(protected_b64 || "." || payload_b64))
    payload_b64 = b64url_encode(json_encode(payload_copy).encode())
    compact = f"{protected_b64}.{payload_b64}.{sig_b64}"

    jws_token = jws.JWS()
    jws_token.deserialize(compact)
    jws_token.verify(key)

    return payload_copy

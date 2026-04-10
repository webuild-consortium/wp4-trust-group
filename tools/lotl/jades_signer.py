"""JAdES Compact Baseline B signing for LoTL JSON."""

import base64
import json
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

    Adds a 'signature' key to the payload with the JAdES structure.

    Args:
        payload: Unsigned JSON-serializable dict (will be modified).
        key_pem: Private key in PEM format.
        cert_pem: Signing certificate in PEM format.
        algorithm: JWS algorithm (RS256, ES256, PS256).

    Returns:
        Payload dict with 'signature' key added.
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
    }

    jws_token = jws.JWS(json_encode(payload))
    jws_token.add_signature(key, None, json_encode(header), None)

    compact = jws_token.serialize(compact=True)
    parts = compact.split(".")

    # JAdES signature structure (protected = JWS protected header)
    payload["signature"] = {
        "protected": header,
        "signature": parts[2],
        "header": {"x5c": [cert_b64]},
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

    protected = sig.get("protected")
    sig_b64 = sig.get("signature")
    x5c = sig.get("header", {}).get("x5c") or (protected.get("x5c") if protected else None)

    if not protected or not sig_b64 or not x5c:
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

    # Rebuild JWS compact: base64url(protected).base64url(payload).signature
    def b64url_encode(data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode().rstrip("=")

    protected_b64 = b64url_encode(json.dumps(protected, separators=(",", ":")).encode())
    payload_b64 = b64url_encode(json_encode(payload_copy).encode())
    compact = f"{protected_b64}.{payload_b64}.{sig_b64}"

    jws_token = jws.JWS()
    jws_token.deserialize(compact)
    jws_token.verify(key)

    return payload_copy

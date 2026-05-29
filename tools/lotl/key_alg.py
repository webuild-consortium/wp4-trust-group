"""Map private key material to JWS and XML-DSig signature algorithms."""

from __future__ import annotations

from typing import Union

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa


def infer_jws_algorithm_from_private_key_pem(key_pem: Union[bytes, str]) -> str:
    """Return JWS ``alg`` (e.g. ES256, RS256) for the given PEM private key."""
    data = key_pem.encode("utf-8") if isinstance(key_pem, str) else key_pem
    key = serialization.load_pem_private_key(data, password=None)
    if isinstance(key, rsa.RSAPrivateKey):
        return "RS256"
    if isinstance(key, ec.EllipticCurvePrivateKey):
        name = key.curve.name
        if name == "secp256r1":
            return "ES256"
        if name == "secp384r1":
            return "ES384"
        if name == "secp521r1":
            return "ES512"
        raise ValueError(f"Unsupported EC curve for JWS: {name}")
    raise ValueError(f"Unsupported private key type for JWS: {type(key).__name__}")


def infer_xml_signature_algorithm_fragment_from_private_key_pem(
    key_pem: Union[bytes, str],
) -> str:
    """Return SignXML ``signature_algorithm`` fragment (e.g. ``rsa-sha256``, ``ecdsa-sha256``)."""
    data = key_pem.encode("utf-8") if isinstance(key_pem, str) else key_pem
    key = serialization.load_pem_private_key(data, password=None)
    if isinstance(key, rsa.RSAPrivateKey):
        return "rsa-sha256"
    if isinstance(key, ec.EllipticCurvePrivateKey):
        name = key.curve.name
        if name == "secp256r1":
            return "ecdsa-sha256"
        if name == "secp384r1":
            return "ecdsa-sha384"
        if name == "secp521r1":
            return "ecdsa-sha512"
        raise ValueError(f"Unsupported EC curve for XML-DSig: {name}")
    raise ValueError(f"Unsupported private key type for XML-DSig: {type(key).__name__}")

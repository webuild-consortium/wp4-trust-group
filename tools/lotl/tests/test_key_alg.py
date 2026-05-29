"""Tests for JWS / XML-DSig algorithm inference from private keys."""

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa

from tools.lotl.key_alg import (
    infer_jws_algorithm_from_private_key_pem,
    infer_xml_signature_algorithm_fragment_from_private_key_pem,
)


def _pem_ec_p256() -> bytes:
    key = ec.generate_private_key(ec.SECP256R1())
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )


def _pem_rsa() -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )


def test_infer_ec_p256_defaults() -> None:
    pem = _pem_ec_p256()
    assert infer_jws_algorithm_from_private_key_pem(pem) == "ES256"
    assert infer_xml_signature_algorithm_fragment_from_private_key_pem(pem) == "ecdsa-sha256"
    assert infer_jws_algorithm_from_private_key_pem(pem.decode("utf-8")) == "ES256"


def test_infer_rsa_defaults() -> None:
    pem = _pem_rsa()
    assert infer_jws_algorithm_from_private_key_pem(pem) == "RS256"
    assert infer_xml_signature_algorithm_fragment_from_private_key_pem(pem) == "rsa-sha256"


def test_infer_ec_secp384() -> None:
    key = ec.generate_private_key(ec.SECP384R1())
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    assert infer_jws_algorithm_from_private_key_pem(pem) == "ES384"
    assert infer_xml_signature_algorithm_fragment_from_private_key_pem(pem) == "ecdsa-sha384"


def test_infer_unsupported_ec_curve() -> None:
    key = ec.generate_private_key(ec.SECP256K1())
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    with pytest.raises(ValueError, match="Unsupported EC curve"):
        infer_jws_algorithm_from_private_key_pem(pem)
    with pytest.raises(ValueError, match="Unsupported EC curve"):
        infer_xml_signature_algorithm_fragment_from_private_key_pem(pem)


def test_infer_ec_secp521() -> None:
    key = ec.generate_private_key(ec.SECP521R1())
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    assert infer_jws_algorithm_from_private_key_pem(pem) == "ES512"
    assert infer_xml_signature_algorithm_fragment_from_private_key_pem(pem) == "ecdsa-sha512"


def test_infer_rejects_ed25519() -> None:
    from cryptography.hazmat.primitives.asymmetric import ed25519

    key = ed25519.Ed25519PrivateKey.generate()
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    with pytest.raises(ValueError, match="Unsupported private key type for JWS"):
        infer_jws_algorithm_from_private_key_pem(pem)
    with pytest.raises(ValueError, match="Unsupported private key type for XML-DSig"):
        infer_xml_signature_algorithm_fragment_from_private_key_pem(pem)

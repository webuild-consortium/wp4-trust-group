"""Certificate path validation against an explicitly configured anchor."""

import base64
import binascii

from cryptography import x509
from OpenSSL import crypto


def decode_certificate_chain(encoded_certs: list[str]) -> list[x509.Certificate]:
    """Decode base64 DER certificates, with the signing certificate first."""
    if not encoded_certs:
        raise ValueError("No signing certificate in signature")
    try:
        return [
            x509.load_der_x509_certificate(base64.b64decode(cert, validate=True))
            for cert in encoded_certs
        ]
    except (ValueError, TypeError, binascii.Error) as exc:
        raise ValueError("Invalid certificate in signature") from exc


def validate_certificate_chain(
    chain: list[x509.Certificate], trust_anchor_pem: str | bytes
) -> None:
    """Validate a signing certificate and intermediates to the configured anchor."""
    if not chain:
        raise ValueError("No signing certificate in signature")
    if isinstance(trust_anchor_pem, str):
        trust_anchor_pem = trust_anchor_pem.encode("utf-8")
    anchor = x509.load_pem_x509_certificate(trust_anchor_pem)
    store = crypto.X509Store()
    store.add_cert(crypto.X509.from_cryptography(anchor))
    store.set_flags(crypto.X509StoreFlags.PARTIAL_CHAIN)
    try:
        crypto.X509StoreContext(
            store,
            crypto.X509.from_cryptography(chain[0]),
            [crypto.X509.from_cryptography(cert) for cert in chain[1:]],
        ).verify_certificate()
    except crypto.X509StoreContextError as exc:
        raise ValueError(f"Certificate chain validation failed: {exc}") from exc

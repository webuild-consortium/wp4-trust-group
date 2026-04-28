"""Pytest fixtures for LoTL tests."""

import sys
from pathlib import Path

# Add project root to path so tools.lotl can be imported
_project_root = Path(__file__).resolve().parents[2]  # tools/lotl/tests -> wp4-trust-group
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

import tempfile

import pytest

from tools.lotl.tl_entry import TLEntry


@pytest.fixture
def signing_key_and_cert(tmp_path: Path) -> tuple[Path, Path]:
    """Generate a temporary RSA key and self-signed certificate for signing tests."""
    import datetime

    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pubkey = key.public_key()
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "EU"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "WP4 Test"),
        x509.NameAttribute(NameOID.COMMON_NAME, "LoTL Test Signer"),
    ])
    now = datetime.datetime.utcnow()
    cert_builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(pubkey)
        .serial_number(1)
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=365))
    )
    # Add extensions required for signxml cert validation
    ski = x509.SubjectKeyIdentifier.from_public_key(pubkey)
    cert_builder = cert_builder.add_extension(ski, critical=False)
    cert_builder = cert_builder.add_extension(
        x509.AuthorityKeyIdentifier.from_issuer_public_key(pubkey),
        critical=False,
    )
    cert_builder = cert_builder.add_extension(
        x509.BasicConstraints(ca=False, path_length=None),
        critical=True,
    )
    cert_builder = cert_builder.add_extension(
        x509.KeyUsage(
            digital_signature=True,
            key_encipherment=False,
            content_commitment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False,
        ),
        critical=True,
    )
    cert_builder = cert_builder.add_extension(
        x509.SubjectAlternativeName([x509.DNSName("localhost")]),
        critical=False,
    )
    cert = cert_builder.sign(key, hashes.SHA256())

    key_path = tmp_path / "key.pem"
    cert_path = tmp_path / "cert.pem"
    key_path.write_bytes(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    return key_path, cert_path


@pytest.fixture
def sample_tl_entry(signing_key_and_cert: tuple[Path, Path]) -> TLEntry:
    """Sample TL entry for tests."""
    _key_path, cert_path = signing_key_and_cert
    return TLEntry(
        tl_type="pid-provider",
        participant_id="example-tlp",
        tl_url="https://example.com/pid_providers.json",
        tl_url_xml="https://example.com/pid_providers.xml",
        trust_anchor=cert_path.read_text(),
        metadata={"operator_name": "Example TLP", "country": "IT"},
    )


@pytest.fixture
def tl_entries_dir(tmp_path: Path, sample_tl_entry: TLEntry) -> Path:
    """Create a temporary tl_entries directory with sample entry."""
    import json

    entry_dir = tmp_path / "pid-provider"
    entry_dir.mkdir()
    entry_file = entry_dir / "example-tlp.json"
    entry_file.write_text(
        json.dumps({
            "tl_url": sample_tl_entry.tl_url,
            "tl_url_xml": sample_tl_entry.tl_url_xml,
            "trust_anchor": sample_tl_entry.trust_anchor,
            "metadata": sample_tl_entry.metadata,
        }, indent=2)
    )
    return tmp_path

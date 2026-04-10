#!/usr/bin/env python3
"""
Create a self-signed, ETSI-compliant X.509 certificate for LoTL/Trusted List signing.

Per ETSI TS 119 612 clause 5.7.1 and Annex B:
- Self-signed (TLSO as issuer)
- Subject DN: C=SchemeTerritory, O=SchemeOperatorName
- KeyUsage: digitalSignature, nonRepudiation
- ExtendedKeyUsage: id-tsl-kp-tslSigning (0.4.0.2231.3.0)
- SubjectKeyIdentifier: present
- BasicConstraints: CA=false
- Key: ECDSA P-256 (minimum 3 years usable per ETSI TS 119 312)
"""

import argparse
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import ExtensionOID, ObjectIdentifier

# ETSI id-tsl-kp-tslSigning OID (TS 119 612 clause 5.7.1)
ID_TSL_KP_TSL_SIGNING = ObjectIdentifier("0.4.0.2231.3.0")


def create_lotl_signing_cert(
    scheme_territory: str,
    scheme_operator_name: str,
    output_dir: Path,
    validity_days: int = 365 * 3,  # 3 years per ETSI TS 119 312
    key_path: Path | None = None,
    cert_path: Path | None = None,
) -> tuple[bytes, bytes]:
    """Generate ETSI-compliant self-signed cert and private key. Returns (key_pem, cert_pem)."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # ECDSA P-256 for minimum 3 years usable key (ETSI TS 119 312)
    key = ec.generate_private_key(ec.SECP256R1())

    subject = issuer = x509.Name(
        [
            x509.NameAttribute(x509.oid.NameOID.COUNTRY_NAME, scheme_territory),
            x509.NameAttribute(x509.oid.NameOID.ORGANIZATION_NAME, scheme_operator_name),
        ]
    )

    now = datetime.now(timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=validity_days))
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                content_commitment=True,  # nonRepudiation
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=False,
                crl_sign=False,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .add_extension(
            x509.ExtendedKeyUsage([ID_TSL_KP_TSL_SIGNING]),
            critical=False,
        )
        .add_extension(
            x509.BasicConstraints(ca=False, path_length=None),
            critical=True,
        )
        .add_extension(
            x509.SubjectKeyIdentifier.from_public_key(key.public_key()),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )

    key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    cert_pem = cert.public_bytes(serialization.Encoding.PEM)

    if key_path:
        key_path.write_bytes(key_pem)
    if cert_path:
        cert_path.write_bytes(cert_pem)

    return key_pem, cert_pem


def _print_cert_diagnostic(cert_path: Path, cert_pem: bytes) -> None:
    """Print certificate diagnostic (ASN.1 / OpenSSL text) and raw PEM."""
    print("--- Certificate (diagnostic ASN / OpenSSL text) ---")
    result = subprocess.run(
        ["openssl", "x509", "-in", str(cert_path), "-text", "-noout"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print(result.stdout)
    else:
        # Fallback: basic Python representation
        cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
        print(f"Certificate:")
        print(f"  Subject: {cert.subject.rfc4514_string()}")
        print(f"  Issuer: {cert.issuer.rfc4514_string()}")
        print(f"  Serial: {cert.serial_number}")
        print(f"  Not Before: {cert.not_valid_before_utc}")
        print(f"  Not After: {cert.not_valid_after_utc}")
        print(f"  Signature: {getattr(cert.signature_algorithm_oid, '_name', cert.signature_algorithm_oid.dotted_string)}")
        for ext in cert.extensions:
            oid_name = getattr(ext.oid, "_name", ext.oid.dotted_string)
            print(f"  {oid_name}: {ext.value}")

    print("--- Certificate (raw PEM) ---")
    print(cert_pem.decode())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create ETSI-compliant self-signed X.509 certificate for LoTL signing",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=Path,
        default=Path("lotl/certs"),
        help="Output directory for key.pem and cert.pem (default: lotl/certs)",
    )
    parser.add_argument(
        "--scheme-territory",
        "-t",
        default="EU",
        help="Scheme territory (ISO 3166-1 alpha-2, e.g. EU, IT) (default: EU)",
    )
    parser.add_argument(
        "--scheme-operator-name",
        "-n",
        default="WP4 Trust Registry Group",
        help="Scheme operator name for Subject/Issuer O (default: WP4 Trust Registry Group)",
    )
    parser.add_argument(
        "--validity-days",
        type=int,
        default=365 * 3,
        help="Certificate validity in days (default: 1095 = 3 years)",
    )
    parser.add_argument(
        "--key-file",
        default="lotl_signing_key.pem",
        help="Output key filename (default: lotl_signing_key.pem)",
    )
    parser.add_argument(
        "--cert-file",
        default="lotl_signing_cert.pem",
        help="Output cert filename (default: lotl_signing_cert.pem)",
    )

    args = parser.parse_args()

    key_path = args.output_dir / args.key_file
    cert_path = args.output_dir / args.cert_file

    try:
        _, cert_pem = create_lotl_signing_cert(
            scheme_territory=args.scheme_territory,
            scheme_operator_name=args.scheme_operator_name,
            output_dir=args.output_dir,
            validity_days=args.validity_days,
            key_path=key_path,
            cert_path=cert_path,
        )
    except OSError as e:
        print(f"Error writing files: {e}", file=sys.stderr)
        return 1

    print(f"Created ETSI-compliant LoTL signing certificate:")
    print(f"  Key:  {key_path}")
    print(f"  Cert: {cert_path}")
    print(f"  Subject: C={args.scheme_territory}, O={args.scheme_operator_name}")
    print()
    print("Use with LoTL producer:")
    print(f"  export LOTL_SIGNING_KEY=$(cat {key_path})")
    print(f"  export LOTL_SIGNING_CERT=$(cat {cert_path})")
    print(f"  python -m tools.lotl --tl-entries-dir lotl/tl_entries/ --output-dir lotl/")
    print()
    print("Or with inline paths:")
    print(f"  python -m tools.lotl --signing-key {key_path} --signing-cert {cert_path} \\")
    print("    --tl-entries-dir lotl/tl_entries/ --output-dir lotl/")
    print()
    _print_cert_diagnostic(cert_path, cert_pem)

    return 0


if __name__ == "__main__":
    sys.exit(main())

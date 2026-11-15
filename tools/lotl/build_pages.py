"""Build the LoTL landing page from the verified signing certificate."""

import argparse
import base64
import json
import os
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization

from tools.lotl.jades_signer import verify_json


def build_pages(template_path: Path, signed_json_path: Path, output_dir: Path, cert_pem: bytes) -> None:
    """Render the page and public PEM files after checking the signed LoTL."""
    cert = x509.load_pem_x509_certificate(cert_pem)
    payload = json.loads(signed_json_path.read_text(encoding="utf-8"))
    verify_json(payload)
    protected = payload["signature"]["protected"]
    header = json.loads(base64.urlsafe_b64decode(protected + "=" * (-len(protected) % 4)))
    signer_der = base64.b64decode(header["x5c"][0], validate=True)
    if signer_der != cert.public_bytes(serialization.Encoding.DER):
        raise ValueError("LoTL signer does not match the configured signing certificate")

    public_key = cert.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_cert = cert.public_bytes(serialization.Encoding.PEM)
    replacements = {
        "<!-- LOTL_SIGNING_PUBLIC_KEY -->": public_key.decode("ascii").strip(),
        "<!-- LOTL_SIGNING_CERT_SHA256 -->": cert.fingerprint(hashes.SHA256()).hex().upper(),
        "<!-- LOTL_SIGNING_CERT_EXPIRY -->": cert.not_valid_after_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
    }
    page = template_path.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        if page.count(placeholder) != 1:
            raise ValueError(f"Expected exactly one {placeholder} placeholder")
        page = page.replace(placeholder, value)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(page, encoding="utf-8")
    (output_dir / "lotl-signing-cert.pem").write_bytes(public_cert)
    (output_dir / "lotl-signing-public-key.pem").write_bytes(public_key)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--signed-json", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    cert = os.environ.get("LOTL_SIGNING_CERT")
    if not cert:
        parser.error("LOTL_SIGNING_CERT must contain the signing certificate")
    build_pages(args.template, args.signed_json, args.output_dir, cert.encode("utf-8"))


if __name__ == "__main__":
    main()

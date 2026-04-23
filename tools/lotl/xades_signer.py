"""XAdES Baseline B signing for LoTL XML."""

from pathlib import Path
from typing import Union

from lxml import etree
from signxml import XMLSigner, XMLVerifier

from tools.lotl.log import get_logger

logger = get_logger(__name__)


def sign_xml(
    xml_content: bytes,
    key_pem: Union[bytes, str, Path],
    cert_pem: Union[bytes, str, Path],
) -> bytes:
    """Sign XML with XAdES Baseline B (enveloped signature).

    Args:
        xml_content: Unsigned XML bytes.
        key_pem: Private key in PEM format.
        cert_pem: Signing certificate in PEM format.

    Returns:
        Signed XML bytes.
    """
    if isinstance(key_pem, Path):
        key_pem = key_pem.read_bytes()
    elif isinstance(key_pem, str) and not key_pem.strip().startswith("-----"):
        key_pem = Path(key_pem).read_bytes()

    if isinstance(cert_pem, Path):
        cert_pem = cert_pem.read_bytes()
    elif isinstance(cert_pem, str) and not cert_pem.strip().startswith("-----"):
        cert_pem = Path(cert_pem).read_bytes()

    if isinstance(key_pem, bytes):
        key_pem = key_pem.decode("utf-8") if isinstance(key_pem, bytes) else key_pem
    if isinstance(cert_pem, bytes):
        cert_pem = cert_pem.decode("utf-8") if isinstance(cert_pem, bytes) else cert_pem

    root = etree.fromstring(xml_content)
    signer = XMLSigner(
        signature_algorithm="rsa-sha256",
        digest_algorithm="sha256",
        c14n_algorithm="http://www.w3.org/2001/10/xml-exc-c14n#",
    )
    signed_root = signer.sign(
        root,
        key=key_pem,
        cert=cert_pem,
        always_add_key_value=False,
    )

    return etree.tostring(
        signed_root,
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
        method="xml",
    )


def verify_xml(
    xml_content: bytes,
    cert_pem: Union[bytes, str, Path] | None = None,
    ca_pem_file: Union[str, Path] | None = None,
) -> bytes:
    """Verify XAdES signature on XML.

    Args:
        xml_content: Signed XML bytes.
        cert_pem: Optional certificate for verification (uses embedded if not provided).
        ca_pem_file: Optional CA file for chain validation (e.g. self-signed cert for tests).

    Returns:
        Verified signed XML.
    """
    root = etree.fromstring(xml_content)
    verifier = XMLVerifier()

    kwargs: dict = {}
    if cert_pem is not None:
        if isinstance(cert_pem, Path):
            cert_pem = cert_pem.read_bytes()
        if isinstance(cert_pem, bytes):
            cert_pem = cert_pem.decode("utf-8")
        kwargs["x509_cert"] = cert_pem
    if ca_pem_file is not None:
        kwargs["ca_pem_file"] = str(ca_pem_file)

    result = verifier.verify(root, **kwargs)

    return etree.tostring(
        result.signed_xml,
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
        method="xml",
    )

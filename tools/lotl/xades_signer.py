"""XAdES Baseline B signing for LoTL XML.

Emits XAdES-B-B per ETSI EN 319 132-1 V1.3.1 Table 2, profiled for trusted lists
by ETSI TS 119 612 V2.4.1 Annex B.1.0.

"""

import datetime
from pathlib import Path
from typing import Union

from lxml import etree
from signxml.exceptions import InvalidSignature
from signxml.xades import (
    XAdESDataObjectFormat,
    XAdESSignatureConfiguration,
    XAdESSigner,
    XAdESVerifier,
)

from tools.lotl.key_alg import (
    infer_xml_signature_algorithm_fragment_from_private_key_pem,
)
from tools.lotl.log import get_logger

logger = get_logger(__name__)

DS = "http://www.w3.org/2000/09/xmldsig#"
XADES = "http://uri.etsi.org/01903/v1.3.2#"
# ETSI TS 119 612 Annex B.1.0 The second transform must use exclusive c14n.
EXC_C14N = "http://www.w3.org/2001/10/xml-exc-c14n#"

# TS 119 612 clause 6.2.2 registers this media type for trusted lists.
TSL_MIME_TYPE = "application/vnd.etsi.tsl+xml"

# The document, SignedProperties and KeyInfo. Only verify_xml's default: EN 319 132-1
# Table 2 gives ds:Reference ">= 2" and TS 119 612 Annex B.1.0 rule 4 permits more.
EXPECTED_REFERENCES = 3

# EN 319 132-1 Table 2 note k requires DataObjectFormat.
DATA_OBJECT_FORMAT = XAdESDataObjectFormat(
    Description="ETSI TS 119 612 trusted list",
    MimeType=TSL_MIME_TYPE,
)


class LoTLXAdESSigner(XAdESSigner):
    """XAdES-B-B signer profiled for trusted lists.
    * **EN 319 132-1** -- ETSI EN 319 132-1 V1.3.1 (2024-07), "XAdES digital
      signatures; Part 1: Building blocks and XAdES baseline signatures". Its
      Table 2 (clause 6.3) is the baseline conformance checklist.
    * **TS 119 612** -- ETSI TS 119 612 V2.4.1 (2025-08), "Trusted Lists". Annex B.1
      constrains a trusted list's signature; clause 5.1.3 constrains date-times.
    """

    def _add_reference_to_signed_info(self, sig_root, node_to_reference, **attrs):
        super()._add_reference_to_signed_info(sig_root, node_to_reference, **attrs)
        reference = self._find(sig_root, "SignedInfo")[-1]
        if reference.find(f"{{{DS}}}Transforms") is None:
            transforms = etree.Element(f"{{{DS}}}Transforms")
            etree.SubElement(transforms, f"{{{DS}}}Transform", Algorithm=EXC_C14N)
            reference.insert(0, transforms)

    def add_signing_time(self, signed_signature_properties, sig_root, signing_settings):
        signing_time = etree.SubElement(
            signed_signature_properties, f"{{{XADES}}}SigningTime"
        )
        signing_time.text = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )


def _parse(xml_content: bytes) -> etree._Element:
    """Parse untrusted XML without DTD loading, entity expansion or network access.

    A LoTL can come from a remote publisher, so guard against XXE and entity
    expansion attacks. lxml parsers must not be shared across threads, so build a
    fresh one per call.
    """
    parser = etree.XMLParser(
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        huge_tree=False,
    )
    return etree.fromstring(xml_content, parser=parser)


def _load_pem(pem: Union[bytes, str, Path]) -> str:
    """Accept a PEM string, PEM bytes, or a path to a PEM file."""
    if isinstance(pem, Path):
        pem = pem.read_bytes()
    elif isinstance(pem, str) and not pem.strip().startswith("-----"):
        pem = Path(pem).read_bytes()
    if isinstance(pem, bytes):
        pem = pem.decode("utf-8")
    return pem


def sign_xml(
    xml_content: bytes,
    key_pem: Union[bytes, str, Path],
    cert_pem: Union[bytes, str, Path],
) -> bytes:
    """Sign XML with XAdES Baseline B.

    Args:
        xml_content: Unsigned XML bytes.
        key_pem: Private key in PEM format.
        cert_pem: Certificate in PEM format.

    Returns:
        Signed XML bytes.
    """
    key_pem = _load_pem(key_pem)
    cert_pem = _load_pem(cert_pem)

    root = _parse(xml_content)

    if not root.get("Id"):
        raise ValueError(
            "Root element needs an Id attribute (TS 119 612 Annex B.1.0 rule 2b)"
        )

    signer = LoTLXAdESSigner(
        signature_algorithm=infer_xml_signature_algorithm_fragment_from_private_key_pem(
            key_pem
        ),
        digest_algorithm="sha256",
        c14n_algorithm=EXC_C14N,
        data_object_format=DATA_OBJECT_FORMAT,
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
    expect_references: int = EXPECTED_REFERENCES,
) -> bytes:
    """Verify the XAdES signature on a LoTL.

    A trust anchor is mandatory. Given neither argument, signxml falls back to the
    certifi CA bundle and validates the embedded certificate as a TLS client
    certificate, so any publicly issued certificate would be accepted as a valid
    LoTL signer.

    Args:
        xml_content: Signed XML bytes.
        cert_pem: Certificate the signature must have been made with.
        ca_pem_file: CA file for chain validation (e.g. a self-signed test cert).
        expect_references: Number of ds:Reference elements the signature must carry.
            Raise this for a signature carrying further references, as TS 119 612
            Annex B.1.0 rule 4 permits.

    Returns:
        The verified, signed XML.

    Raises:
        ValueError: If neither cert_pem nor ca_pem_file is given. The caller is at
            fault; nothing was read from xml_content.
        InvalidSignature: If the list must not be trusted -- it carries other than
            exactly one signature, or no ds:Reference covers the list itself.
            signxml raises the same type for a bad digest, key or certificate, so
            one handler covers every "do not trust this list" outcome.
    """
    if cert_pem is None and ca_pem_file is None:
        raise ValueError(
            "A trust anchor is required: pass cert_pem or ca_pem_file."
        )

    root = _parse(xml_content)

    # Annex B.0 binds the XML schema, whose TrustStatusListType declares
    # ds:Signate with an implicit maxOccurs="1". signxml verifies only the first
    # ds:Signature it finds, so reject extras rather than silently ignores them 
    signatures = root.findall(f"{{{DS}}}Signature")
    if len(signatures) != 1:
        raise InvalidSignature(
            f"A trusted list carries exactly one signature, found {len(signatures)}"
        )

    root_id = root.get("Id")
    if not root_id:
        raise InvalidSignature(
            "Root element carries no Id, so no ds:Reference can cover it "
            "(TS 119 612 Annex B.1.0 rule 2b)"
        )

    kwargs: dict = {}
    if cert_pem is not None:
        kwargs["x509_cert"] = _load_pem(cert_pem)
    if ca_pem_file is not None:
        kwargs["ca_pem_file"] = str(ca_pem_file)

    results = XAdESVerifier().verify(
        root,
        expect_config=XAdESSignatureConfiguration(expect_references=expect_references),
        **kwargs,
    )

    # Annex B.1.0 rule 2: a ds:Reference covers the TrustServiceStatusList itself.
    # Select that reference by the root's Id
    verified = results if isinstance(results, list) else [results]
    covered = [
        result.signed_xml
        for result in verified
        if result.signed_xml is not None
        and result.signed_xml.tag == root.tag
        and result.signed_xml.get("Id") == root_id
    ]
    if len(covered) != 1:
        raise InvalidSignature(
            f"Expected exactly one ds:Reference covering the trusted list "
            f"#{root_id}, found {len(covered)}"
        )
    signed_xml = covered[0]

    return etree.tostring(
        signed_xml,
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
        method="xml",
    )

"""Certificate paths for published JSON and XML list signatures."""

import base64
import json
from datetime import datetime, timedelta, timezone

import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import NameOID
from jwcrypto import jwk, jws
from jwcrypto.common import json_encode
from lxml import etree

from tools.lotl.tl_validator import validate_tl_signature_json, validate_tl_signature_xml
from tools.lotl.xades_signer import sign_xml
from tools.lotl.xml_generator import generate_lotl_xml


def make_cert(name, *, issuer=None, ca=False, path_length=None, expired=False):
    key = ec.generate_private_key(ec.SECP256R1())
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, name)])
    issuer_key, issuer_cert = issuer if issuer else (key, None)
    now = datetime.now(timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer_cert.subject if issuer_cert else subject)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=10))
        .not_valid_after(now - timedelta(days=1) if expired else now + timedelta(days=10))
        .add_extension(x509.BasicConstraints(ca=ca, path_length=path_length), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True, content_commitment=False, key_encipherment=False,
                data_encipherment=False, key_agreement=False, key_cert_sign=ca,
                crl_sign=ca, encipher_only=False, decipher_only=False,
            ),
            critical=True,
        )
        .sign(issuer_key, hashes.SHA256())
    )
    return key, cert


def pem(cert):
    return cert.public_bytes(serialization.Encoding.PEM)


def signed_json(key, chain):
    key_pem = key.private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    header = {
        "alg": "ES256",
        "x5c": [base64.b64encode(c.public_bytes(serialization.Encoding.DER)).decode()
                for c in chain],
    }
    token = jws.JWS(json_encode({"message": "test"}))
    token.add_signature(jwk.JWK.from_pem(key_pem), protected=json_encode(header))
    protected, _, signature = token.serialize(compact=True).split(".")
    return {"message": "test", "signature": {"protected": protected, "signature": signature}}


def signed_xml(key, chain):
    key_pem = key.private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    return sign_xml(generate_lotl_xml([], sequence_number=1), key_pem, b"".join(map(pem, chain)))


@pytest.mark.parametrize("format", ["json", "xml"])
def test_direct_and_ca_anchor_paths(format):
    root = make_cert("root", ca=True)
    intermediate = make_cert("intermediate", issuer=root, ca=True)
    leaf = make_cert("leaf", issuer=intermediate)
    direct_leaf = make_cert("direct leaf", issuer=root)

    def validate(key, chain, anchor):
        if format == "json":
            return validate_tl_signature_json(json.dumps(signed_json(key, chain)), pem(anchor).decode())
        return validate_tl_signature_xml(signed_xml(key, chain), pem(anchor).decode())

    # The anchor need not appear in the signature; it may itself be non-self-signed.
    for key, chain, anchor in [
        (direct_leaf[0], [direct_leaf[1]], direct_leaf[1]),
        (direct_leaf[0], [direct_leaf[1]], root[1]),
        (leaf[0], [leaf[1], intermediate[1]], root[1]),
        (leaf[0], [leaf[1]], intermediate[1]),
        (leaf[0], [leaf[1], intermediate[1], root[1]], root[1]),
    ]:
        valid, error = validate(key, chain, anchor)
        assert valid, error


@pytest.mark.parametrize("format", ["json", "xml"])
@pytest.mark.parametrize(
    "problem", ["untrusted", "missing_intermediate", "expired", "not_ca", "path_length", "bad_signature"]
)
def test_invalid_paths_fail(format, problem):
    root = make_cert("root", ca=True, path_length=0 if problem == "path_length" else None)
    intermediate = make_cert("intermediate", issuer=root, ca=problem != "not_ca")
    leaf = make_cert("leaf", issuer=intermediate, expired=problem == "expired")
    chain = [leaf[1], intermediate[1]]
    anchor = root[1]
    if problem == "untrusted":
        anchor = make_cert("other", ca=True)[1]
    elif problem == "missing_intermediate":
        chain = [leaf[1]]
    elif problem == "bad_signature":
        fake_root = make_cert("root", ca=True)
        leaf = make_cert("leaf", issuer=fake_root)
        chain = [leaf[1]]
    if format == "json":
        valid, error = validate_tl_signature_json(json.dumps(signed_json(leaf[0], chain)), pem(anchor).decode())
    else:
        valid, error = validate_tl_signature_xml(signed_xml(leaf[0], chain), pem(anchor).decode())
    assert not valid
    assert "Certificate chain validation failed" in error


def test_json_rejects_tampering_and_missing_anchor():
    root = make_cert("root", ca=True)
    leaf = make_cert("leaf", issuer=root)
    payload = signed_json(leaf[0], [leaf[1]])
    payload["message"] = "tampered"
    valid, _ = validate_tl_signature_json(json.dumps(payload), pem(root[1]).decode())
    assert not valid
    valid, _ = validate_tl_signature_json(json.dumps(signed_json(leaf[0], [leaf[1]])), "")
    assert not valid
    valid, _ = validate_tl_signature_json(json.dumps(signed_json(leaf[0], [leaf[1]])), None)
    assert not valid


def test_xml_rejects_tampering():
    root = make_cert("root", ca=True)
    leaf = make_cert("leaf", issuer=root)
    signed = signed_xml(leaf[0], [leaf[1]])
    document = etree.fromstring(signed)
    document.set("tampered", "yes")
    valid, _ = validate_tl_signature_xml(etree.tostring(document), pem(root[1]).decode())
    assert not valid


@pytest.mark.parametrize("format", ["json", "xml"])
def test_expired_direct_anchor_rejected(format):
    leaf = make_cert("expired", expired=True)
    if format == "json":
        valid, error = validate_tl_signature_json(json.dumps(signed_json(leaf[0], [leaf[1]])), pem(leaf[1]).decode())
    else:
        valid, error = validate_tl_signature_xml(signed_xml(leaf[0], [leaf[1]]), pem(leaf[1]).decode())
    assert not valid
    assert "Certificate chain validation failed" in error

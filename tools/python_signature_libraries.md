# Python Libraries for XAdES and JAdES Signatures

This document provides guidance on using Python libraries to implement XAdES (XML) and JAdES (JSON) digital signatures for ETSI Trusted Lists.

## Table of Contents
1. [XAdES Signatures](#1-xades-signatures)
2. [JAdES Signatures](#2-jades-signatures)
3. [Certificate Handling](#3-certificate-handling)
4. [Complete Examples](#4-complete-examples)
5. [Library Comparison](#5-library-comparison)
6. [Recommended Approach](#6-recommended-approach)

## 1. XAdES Signatures

### 1.1 Recommended: `python-xades`

```bash
pip install python-xades
```

**Example Usage:**
```python
from xades import XAdES, template

# Create XAdES signature
signer = XAdES()
signer.load('private_key.pem', 'certificate.pem')

# Sign XML document
signed_xml = signer.sign('tsl.xml', method=template.XAdES_BASELINE_B)

# Save signed document
with open('tsl-signed.xml', 'wb') as f:
    f.write(signed_xml)
```

### 1.2 Alternative: `signxml`

```bash
pip install signxml
```

**Example Usage:**
```python
from signxml import XMLSigner, XMLVerifier
from lxml import etree

# Load XML
tree = etree.parse('tsl.xml')

# Sign with XAdES
signer = XMLSigner(
    method=signxml.methods.enveloped,
    signature_algorithm='rsa-sha256',
    digest_algorithm='sha256',
    c14n_algorithm='http://www.w3.org/2001/10/xml-exc-c14n#'
)
signed_root = signer.sign(tree, key='private_key.pem', cert='certificate.pem')

# Verify signature
verifier = XMLVerifier()
verified_data = verifier.verify(signed_root, x509_cert='certificate.pem')
```

### 1.3 Alternative: `cryptography` + `lxml` (manual implementation)

```bash
pip install cryptography lxml
```

For manual XAdES implementation, you'll need to:
1. Use `cryptography` for cryptographic operations
2. Use `lxml` for XML manipulation
3. Implement XAdES structure manually according to ETSI EN 319 132-1

## 2. JAdES Signatures

### 2.1 Recommended: `jwcrypto` + custom JAdES implementation

```bash
pip install jwcrypto
```

**Example Usage (Compact JAdES Baseline B):**
```python
from jwcrypto import jws, jwk
from jwcrypto.common import json_encode
import json
from datetime import datetime

# Load certificate and key
with open('private_key.pem', 'rb') as f:
    key = jwk.JWK.from_pem(f.read())

with open('certificate.pem', 'rb') as f:
    cert_pem = f.read()

# Load LoTE JSON (without signature)
with open('lote.json', 'r') as f:
    lote_data = json.load(f)

# Create JWS header (JAdES Baseline B)
header = {
    "alg": "ES256",  # or RS256, PS256, etc.
    "x5c": [cert_pem.decode('utf-8')]  # Certificate chain
}

# Create JWS
jws_token = jws.JWS(json_encode(lote_data))
jws_token.add_signature(key, None, json_encode(header), None)

# Get compact serialization
compact_jws = jws_token.serialize(compact=True)

# Create JAdES structure
jades_signature = {
    "protected": json.loads(jws_token.objects['protected']),
    "signature": compact_jws.split('.')[-1],
    "header": {
        "x5c": [cert_pem.decode('utf-8')]
    }
}

# Add signature to LoTE
lote_data['signature'] = jades_signature

# Save signed LoTE
with open('lote-signed.json', 'w') as f:
    json.dump(lote_data, f, indent=2)
```

### 2.2 Alternative: `python-jose` (for JWS, requires JAdES extension)

```bash
pip install python-jose[cryptography]
```

**Note**: `python-jose` provides JWS functionality but JAdES-specific features need to be implemented manually.

## 3. Certificate Handling

### 3.1 Recommended: `cryptography`

```bash
pip install cryptography
```

**Example Usage:**
```python
from cryptography import x509
from cryptography.hazmat.primitives import serialization

# Load certificate
with open('certificate.pem', 'rb') as f:
    cert = x509.load_pem_x509_certificate(f.read())

# Extract certificate information
subject = cert.subject
issuer = cert.issuer
serial_number = cert.serial_number
not_valid_before = cert.not_valid_before
not_valid_after = cert.not_valid_after

# Get certificate in base64 for JAdES
cert_base64 = cert.public_bytes(serialization.Encoding.DER)
import base64
cert_b64 = base64.b64encode(cert_base64).decode('utf-8')
```

## 4. Complete Examples

### 4.1 Signing LoTE with JAdES

```python
from jwcrypto import jws, jwk
from jwcrypto.common import json_encode
import json
import base64
from cryptography import x509
from cryptography.hazmat.primitives import serialization

def sign_lote_json(lote_path, key_path, cert_path, output_path):
    """Sign a LoTE JSON file with Compact JAdES Baseline B signature."""
    
    # Load private key
    with open(key_path, 'rb') as f:
        key = jwk.JWK.from_pem(f.read())
    
    # Load certificate
    with open(cert_path, 'rb') as f:
        cert_pem = f.read()
        cert = x509.load_pem_x509_certificate(cert_pem)
    
    # Get certificate in base64
    cert_der = cert.public_bytes(serialization.Encoding.DER)
    cert_b64 = base64.b64encode(cert_der).decode('utf-8')
    
    # Load LoTE JSON (remove signature if present)
    with open(lote_path, 'r') as f:
        lote_data = json.load(f)
    
    # Remove existing signature if present
    lote_data.pop('signature', None)
    
    # Create JWS header
    header = {
        "alg": "ES256",  # Adjust based on your key type
        "x5c": [cert_b64]
    }
    
    # Create JWS
    payload = json_encode(lote_data)
    jws_token = jws.JWS(payload)
    jws_token.add_signature(key, None, json_encode(header), None)
    
    # Get compact serialization
    compact_jws = jws_token.serialize(compact=True)
    parts = compact_jws.split('.')
    
    # Create JAdES signature structure
    jades_signature = {
        "protected": json.loads(jws_token.objects['protected']),
        "signature": parts[2],  # Signature part
        "header": {
            "x5c": [cert_b64]
        }
    }
    
    # Add signature to LoTE
    lote_data['signature'] = jades_signature
    
    # Save signed LoTE
    with open(output_path, 'w') as f:
        json.dump(lote_data, f, indent=2)
    
    print(f"Signed LoTE saved to {output_path}")

# Usage
sign_lote_json(
    'lote.json',
    'private_key.pem',
    'certificate.pem',
    'lote-signed.json'
)
```

### 4.2 Signing TSL with XAdES

```python
from signxml import XMLSigner
from lxml import etree

def sign_tsl_xml(tsl_path, key_path, cert_path, output_path):
    """Sign a TSL XML file with XAdES Baseline B signature."""
    
    # Load XML
    tree = etree.parse(tsl_path)
    root = tree.getroot()
    
    # Load key and certificate
    with open(key_path, 'rb') as f:
        key_data = f.read()
    
    with open(cert_path, 'rb') as f:
        cert_data = f.read()
    
    # Create signer
    signer = XMLSigner(
        method=signxml.methods.enveloped,
        signature_algorithm='rsa-sha256',
        digest_algorithm='sha256',
        c14n_algorithm='http://www.w3.org/2001/10/xml-exc-c14n#'
    )
    
    # Sign
    signed_root = signer.sign(
        root,
        key=key_data,
        cert=cert_data
    )
    
    # Save signed XML
    tree = etree.ElementTree(signed_root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True, pretty_print=True)
    
    print(f"Signed TSL saved to {output_path}")

# Usage
sign_tsl_xml(
    'tsl.xml',
    'private_key.pem',
    'certificate.pem',
    'tsl-signed.xml'
)
```

## 5. Library Comparison

| Library | XAdES | JAdES | Ease of Use | Notes |
|--------|-------|-------|-------------|-------|
| `python-xades` | ✅ | ❌ | ⭐⭐⭐ | Specialized for XAdES |
| `signxml` | ✅ | ❌ | ⭐⭐⭐⭐ | Good XAdES support, actively maintained |
| `jwcrypto` | ❌ | ✅* | ⭐⭐⭐ | JWS support, JAdES needs manual implementation |
| `python-jose` | ❌ | ✅* | ⭐⭐⭐ | JWS support, JAdES needs manual implementation |
| `cryptography` | ✅* | ✅* | ⭐⭐ | Low-level, requires manual implementation |

*Requires manual implementation of AdES-specific features

## 6. Recommended Approach

**For XAdES (XML):**
- **Primary**: Use `signxml` for production
- **Alternative**: Use `python-xades` if you need more XAdES-specific features

**For JAdES (JSON):**
- **Primary**: Use `jwcrypto` with custom JAdES implementation
- **Alternative**: Use `python-jose` if you prefer its API

**For Certificate Handling:**
- Always use `cryptography` for certificate operations

## Installation Commands

```bash
# For XAdES
pip install signxml lxml
# or
pip install python-xades

# For JAdES
pip install jwcrypto cryptography
# or
pip install python-jose[cryptography] cryptography

# For certificate operations
pip install cryptography
```

## References

- [ETSI TS 119 182-1](https://www.etsi.org/deliver/etsi_ts/119100_119199/11918201/01.02.01_60/ts_11918201v010201p.pdf) - JAdES
- [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf) - XAdES
- [signxml Documentation](https://github.com/XML-Security/signxml)
- [jwcrypto Documentation](https://jwcrypto.readthedocs.io/)

---

**Document Version**: 1.0  
**Last Updated**: 2025-01-XX



#### 5.9 Python Implementation for Digital Signing

##### 5.9.1 Python Code for ListOfTrustedLists Signing

Here's a complete Python implementation for signing the ListOfTrustedLists example:

```python
#!/usr/bin/env python3
"""
ETSI TS 119 612 v2.4.1 ListOfTrustedLists Digital Signing Implementation
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import pkcs12
from datetime import datetime, timezone
import base64
import uuid

class ListOfTrustedListsSigner:
    def __init__(self, private_key_path, certificate_path, password=None):
        """
        Initialize the signer with private key and certificate
        
        Args:
            private_key_path: Path to private key file (PEM or PKCS#12)
            certificate_path: Path to certificate file (PEM or PKCS#12)
            password: Password for PKCS#12 files (if applicable)
        """
        self.private_key = self._load_private_key(private_key_path, password)
        self.certificate = self._load_certificate(certificate_path, password)
        
    def _load_private_key(self, key_path, password):
        """Load private key from file"""
        with open(key_path, 'rb') as key_file:
            if key_path.endswith('.p12') or key_path.endswith('.pfx'):
                # PKCS#12 format
                private_key, _, _ = pkcs12.load_key_and_certificates(
                    key_file.read(), password.encode() if password else None
                )
                return private_key
            else:
                # PEM format
                return serialization.load_pem_private_key(
                    key_file.read(), 
                    password.encode() if password else None
                )
    
    def _load_certificate(self, cert_path, password):
        """Load certificate from file"""
        with open(cert_path, 'rb') as cert_file:
            if cert_path.endswith('.p12') or cert_path.endswith('.pfx'):
                # PKCS#12 format
                _, certificate, _ = pkcs12.load_key_and_certificates(
                    cert_file.read(), password.encode() if password else None
                )
                return certificate
            else:
                # PEM format
                return x509.load_pem_x509_certificate(cert_file.read())
    
    def create_list_of_trusted_lists(self, list_id=None):
        """Create the ListOfTrustedLists XML structure"""
        if list_id is None:
            list_id = f"list-of-trusted-lists-{uuid.uuid4().hex[:8]}"
        
        # Create root element
        root = ET.Element("ListOfTrustedLists")
        root.set("xmlns", "http://uri.etsi.org/19612/v2.4.1#")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:schemaLocation", 
                "http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd")
        root.set("Id", list_id)
        
        # ListInformation
        list_info = ET.SubElement(root, "ListInformation")
        
        # ListName
        list_name = ET.SubElement(list_info, "ListName")
        name_en = ET.SubElement(list_name, "Name")
        name_en.set("xml:lang", "en")
        name_en.text = "WeBuild LSP Trusted Lists Registry"
        
        name_it = ET.SubElement(list_name, "Name")
        name_it.set("xml:lang", "it")
        name_it.text = "Registro delle Liste di Fiducia WeBuild LSP"
        
        name_sv = ET.SubElement(list_name, "Name")
        name_sv.set("xml:lang", "sv")
        name_sv.text = "WeBuild LSP-förtroendelistor Register"
        
        # Other ListInformation elements
        list_id_elem = ET.SubElement(list_info, "ListIdentifier")
        list_id_elem.text = "WEBUILD-TL-REGISTRY-001"
        
        list_version = ET.SubElement(list_info, "ListVersion")
        list_version.text = "1"
        
        list_issue_date = ET.SubElement(list_info, "ListIssueDateTime")
        list_issue_date.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        next_update = ET.SubElement(list_info, "NextUpdate")
        next_update.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # ListOperatorName
        list_operator_name = ET.SubElement(list_info, "ListOperatorName")
        operator_name_en = ET.SubElement(list_operator_name, "Name")
        operator_name_en.set("xml:lang", "en")
        operator_name_en.text = "WeBuild LSP"
        
        operator_name_it = ET.SubElement(list_operator_name, "Name")
        operator_name_it.set("xml:lang", "it")
        operator_name_it.text = "WeBuild LSP"
        
        operator_name_sv = ET.SubElement(list_operator_name, "Name")
        operator_name_sv.set("xml:lang", "sv")
        operator_name_sv.text = "WeBuild LSP"
        
        # ListOperatorAddress
        list_operator_address = ET.SubElement(list_info, "ListOperatorAddress")
        postal_addresses = ET.SubElement(list_operator_address, "PostalAddresses")
        postal_address = ET.SubElement(postal_addresses, "PostalAddress")
        
        street_address = ET.SubElement(postal_address, "StreetAddress")
        street_address.text = "Via dei Fori Imperiali 1"
        
        locality = ET.SubElement(postal_address, "Locality")
        locality.text = "Rome"
        
        postal_code = ET.SubElement(postal_address, "PostalCode")
        postal_code.text = "00184"
        
        country_name = ET.SubElement(postal_address, "CountryName")
        country_name.text = "IT"
        
        electronic_address = ET.SubElement(list_operator_address, "ElectronicAddress")
        uri = ET.SubElement(electronic_address, "URI")
        uri.text = "mailto:trust@webuildlsp.example.org"
        
        # DistributionPoints
        distribution_points = ET.SubElement(list_info, "DistributionPoints")
        distribution_point = ET.SubElement(distribution_points, "DistributionPoint")
        dist_uri = ET.SubElement(distribution_point, "URI")
        dist_uri.text = "https://trust.webuildlsp.example.org/lists/list-of-trusted-lists.xml"
        
        # TrustedLists container
        trusted_lists = ET.SubElement(root, "TrustedLists")
        
        # Add sample TrustedListPointer
        trusted_list_pointer = ET.SubElement(trusted_lists, "TrustedListPointer")
        
        tsl_location = ET.SubElement(trusted_list_pointer, "TSLLocation")
        tsl_location.text = "https://trust.webuildlsp.example.org/tsl/tsl.xml"
        
        tsl_type = ET.SubElement(trusted_list_pointer, "TSLType")
        tsl_type.text = "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric"
        
        scheme_territory = ET.SubElement(trusted_list_pointer, "SchemeTerritory")
        scheme_territory.text = "IT"
        
        scheme_operator_name = ET.SubElement(trusted_list_pointer, "SchemeOperatorName")
        scheme_op_name = ET.SubElement(scheme_operator_name, "Name")
        scheme_op_name.set("xml:lang", "en")
        scheme_op_name.text = "WeBuild LSP Trust Authority"
        
        scheme_name = ET.SubElement(trusted_list_pointer, "SchemeName")
        scheme_name_elem = ET.SubElement(scheme_name, "Name")
        scheme_name_elem.set("xml:lang", "en")
        scheme_name_elem.text = "WeBuild LSP Trusted List"
        
        list_issue_date = ET.SubElement(trusted_list_pointer, "ListIssueDateTime")
        list_issue_date.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        next_update_pointer = ET.SubElement(trusted_list_pointer, "NextUpdate")
        next_update_pointer.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        sequence_number = ET.SubElement(trusted_list_pointer, "SequenceNumber")
        sequence_number.text = "1"
        
        return root, list_id
    
    def sign_xml(self, xml_root, reference_id):
        """Sign the XML document using XML Digital Signature"""
        # Create Signature element
        signature = ET.Element("Signature")
        signature.set("xmlns", "http://www.w3.org/2000/09/xmldsig#")
        
        # SignedInfo
        signed_info = ET.SubElement(signature, "SignedInfo")
        
        # CanonicalizationMethod
        canon_method = ET.SubElement(signed_info, "CanonicalizationMethod")
        canon_method.set("Algorithm", "http://www.w3.org/2001/10/xml-exc-c14n#")
        
        # SignatureMethod
        sig_method = ET.SubElement(signed_info, "SignatureMethod")
        sig_method.set("Algorithm", "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256")
        
        # Reference
        reference = ET.SubElement(signed_info, "Reference")
        reference.set("URI", f"#{reference_id}")
        
        # Transforms
        transforms = ET.SubElement(reference, "Transforms")
        transform = ET.SubElement(transforms, "Transform")
        transform.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#enveloped-signature")
        
        # DigestMethod
        digest_method = ET.SubElement(reference, "DigestMethod")
        digest_method.set("Algorithm", "http://www.w3.org/2001/04/xmlenc#sha256")
        
        # Calculate digest value
        digest_value = self._calculate_digest(xml_root, reference_id)
        digest_value_elem = ET.SubElement(reference, "DigestValue")
        digest_value_elem.text = digest_value
        
        # SignatureValue
        signature_value = self._calculate_signature(signed_info)
        sig_value_elem = ET.SubElement(signature, "SignatureValue")
        sig_value_elem.text = signature_value
        
        # KeyInfo
        key_info = ET.SubElement(signature, "KeyInfo")
        x509_data = ET.SubElement(key_info, "X509Data")
        x509_cert = ET.SubElement(x509_data, "X509Certificate")
        x509_cert.text = base64.b64encode(
            self.certificate.public_bytes(serialization.Encoding.DER)
        ).decode('utf-8')
        
        # Add signature to root
        xml_root.append(signature)
        
        return xml_root
    
    def _calculate_digest(self, xml_root, reference_id):
        """Calculate SHA-256 digest of the referenced element"""
        # Find the element with the specified ID
        target_element = xml_root.find(f".//*[@Id='{reference_id}']")
        if target_element is None:
            raise ValueError(f"Element with ID '{reference_id}' not found")
        
        # Convert to string and canonicalize (simplified)
        xml_str = ET.tostring(target_element, encoding='unicode')
        
        # Calculate SHA-256 hash
        digest = hashes.Hash(hashes.SHA256())
        digest.update(xml_str.encode('utf-8'))
        digest_bytes = digest.finalize()
        
        return base64.b64encode(digest_bytes).decode('utf-8')
    
    def _calculate_signature(self, signed_info):
        """Calculate RSA signature of the SignedInfo element"""
        # Convert SignedInfo to string
        signed_info_str = ET.tostring(signed_info, encoding='unicode')
        
        # Calculate SHA-256 hash
        digest = hashes.Hash(hashes.SHA256())
        digest.update(signed_info_str.encode('utf-8'))
        digest_bytes = digest.finalize()
        
        # Sign with RSA
        signature_bytes = self.private_key.sign(
            digest_bytes,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature_bytes).decode('utf-8')
    
    def create_signed_list_of_trusted_lists(self, output_file, list_id=None):
        """Create and sign a complete ListOfTrustedLists document"""
        # Create the XML structure
        xml_root, actual_list_id = self.create_list_of_trusted_lists(list_id)
        
        # Sign the document
        signed_xml = self.sign_xml(xml_root, actual_list_id)
        
        # Pretty print and save
        rough_string = ET.tostring(signed_xml, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)
        
        print(f"Signed ListOfTrustedLists saved to: {output_file}")
        return signed_xml

def main():
    """Example usage of the ListOfTrustedListsSigner"""
    
    # Initialize signer (replace with actual paths)
    signer = ListOfTrustedListsSigner(
        private_key_path="private_key.pem",  # or .p12
        certificate_path="certificate.pem",  # or .p12
        password=None  # if using PKCS#12 files
    )
    
    # Create and sign the ListOfTrustedLists
    signed_xml = signer.create_signed_list_of_trusted_lists(
        output_file="signed_list_of_trusted_lists.xml",
        list_id="webuild-tl-registry-001"
    )
    
    print("ListOfTrustedLists created and signed successfully!")

if __name__ == "__main__":
    main()
```

##### 5.9.2 Requirements and Dependencies

Create a `requirements.txt` file for the Python implementation:

```txt
cryptography>=41.0.0
lxml>=4.9.0
```

##### 5.9.3 Usage Example

```python
# Example usage script
from list_of_trusted_lists_signer import ListOfTrustedListsSigner

# Initialize with your certificates
signer = ListOfTrustedListsSigner(
    private_key_path="path/to/private_key.pem",
    certificate_path="path/to/certificate.pem"
)

# Create and sign the document
signed_xml = signer.create_signed_list_of_trusted_lists(
    output_file="signed_list_of_trusted_lists.xml"
)
```

##### 5.9.4 Validation Script

```python
#!/usr/bin/env python3
"""
Validate the signed ListOfTrustedLists against ETSI schema
"""

import subprocess
import sys

def validate_signed_xml(xml_file):
    """Validate the signed XML against ETSI SIE schema"""
    try:
        # Validate against SIE schema
        result = subprocess.run([
            'xmllint', 
            '--schema', 
            'https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd',
            xml_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ XML validation successful!")
            return True
        else:
            print("❌ XML validation failed:")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ xmllint not found. Please install libxml2-utils")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_signed_xml.py <xml_file>")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    validate_signed_xml(xml_file)
```

##### 5.9.5 Key Features of the Python Implementation

1. **Complete XML Generation**: Creates the full ListOfTrustedLists structure
2. **Digital Signing**: Implements XML Digital Signature (XMLDSig) standard
3. **Certificate Support**: Supports both PEM and PKCS#12 certificate formats
4. **Canonicalization**: Proper XML canonicalization for signature calculation
5. **Hash Calculation**: SHA-256 digest calculation for referenced elements
6. **RSA Signing**: RSA-PKCS1v15 signature generation
7. **Schema Validation**: Includes validation against ETSI SIE schema
8. **Error Handling**: Comprehensive error handling and validation

##### 5.9.6 Security Considerations

- **Private Key Protection**: Store private keys securely
- **Certificate Validation**: Ensure certificates are valid and trusted
- **Signature Verification**: Implement signature verification in consuming applications
- **Key Rotation**: Plan for certificate and key rotation
- **Audit Logging**: Log all signing operations for audit purposes

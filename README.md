# CertExplorer

A Python tool to convert raw hexadecimal certificate data into a human-readable format.

## Installation
```bash
pip install -r requirements.txt
````

## Usage

```python
import binascii
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Convert hex to bytes
hex_cert = "<your-hex-certificate>"
cert_bytes = binascii.unhexlify(hex_cert)

# Load certificate
cert = x509.load_pem_x509_certificate(cert_bytes, default_backend())

# Print human-readable certificate info
print(cert.subject)
print(cert.issuer)
print(cert.not_valid_before)
print(cert.not_valid_after)
```

## Contributing

Feel free to open an issue or pull request for improvements!

```

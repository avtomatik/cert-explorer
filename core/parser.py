import binascii

from cryptography import x509
from cryptography.hazmat.backends import default_backend


def parse_certificate_from_hex(raw_certificate: str) -> x509.Certificate:
    cert_bytes = binascii.unhexlify(raw_certificate[2:])
    return x509.load_der_x509_certificate(cert_bytes, default_backend())


def get_certificate_info(cert: x509.Certificate) -> dict:
    return {
        "subject": cert.subject,
        "issuer": cert.issuer,
        "not_valid_before": cert.not_valid_before_utc,
        "not_valid_after": cert.not_valid_after_utc,
    }

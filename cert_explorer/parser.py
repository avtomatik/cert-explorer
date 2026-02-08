import binascii

from cryptography import x509
from cryptography.hazmat.backends import default_backend


def parse_certificate_from_hex(raw_certificate: str):
    """
    Converts raw hexadecimal certificate to a human-readable x509 certificate.

    Args:
        raw_certificate (str): Hexadecimal string representing the certificate
        (with '0x' prefix).

    Returns:
        x509.Certificate: Parsed certificate object.
    """
    cert_bytes = binascii.unhexlify(raw_certificate[2:])
    return x509.load_der_x509_certificate(cert_bytes, default_backend())


def get_certificate_info(cert: x509.Certificate):
    """
    Extracts key information from the x509 certificate.

    Args:
        cert (x509.Certificate): The parsed certificate object.

    Returns:
        dict: Dictionary containing certificate details.
    """
    return {
        "subject": cert.subject,
        "issuer": cert.issuer,
        "not_valid_before": cert.not_valid_before_utc,
        "not_valid_after": cert.not_valid_after_utc,
    }

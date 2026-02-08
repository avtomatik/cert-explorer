from cryptography.hazmat.primitives import serialization

from core.interfaces import CertificateSource, CertificateWriter
from core.parser import get_certificate_info, parse_certificate_from_hex


class CertificateProcessor:
    """Processes certificates atomically from a source to a writer."""

    def __init__(self, source: CertificateSource, writer: CertificateWriter):
        self.source = source
        self.writer = writer

    def process_certificate(self, i: int, entry: dict):
        """Process a single raw certificate entry atomically."""
        raw_certificate = entry.get("RawCertificate")
        if not raw_certificate:
            print(f"Entry {i} has no RawCertificate field, skipping.")
            return

        try:
            cert = parse_certificate_from_hex(raw_certificate)
            info = get_certificate_info(cert)

            # Print certificate info
            for key, value in info.items():
                print(f"{key}: {value}")

            # Atomic write
            file_path = self.writer.write_atomic(
                cert.public_bytes(encoding=serialization.Encoding.DER),
                name_hint=f"cert_{i:06}",
            )
            print(f"Saved certificate to {file_path}")

        except Exception as e:
            print(f"Failed to process certificate {i}: {e}.")

    def process_all(self):
        """Process all certificates from the source."""
        for i, entry in enumerate(self.source.get_raw_certificates()):
            self.process_certificate(i, entry)

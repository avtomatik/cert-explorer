from pathlib import Path

from core.io import FileCertificateWriter, JSONCertificateSource
from core.processor import CertificateProcessor


def main():
    source = JSONCertificateSource(Path("data/dump.json"))
    writer = FileCertificateWriter(Path("certificates"))
    processor = CertificateProcessor(source, writer)
    processor.process_all()


if __name__ == "__main__":
    main()

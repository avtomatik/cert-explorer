from pathlib import Path


def write_cert_to_file(cert_bytes: bytes, file_path: Path) -> Path:
    """
    Writes the certificate bytes to a file.

    Args:
        cert_bytes (bytes): The certificate's byte representation.
        file_path (pathlib.Path): The output file path.
    """
    with file_path.open("wb") as f:
        f.write(cert_bytes)

def write_cert_to_file(cert_bytes: bytes, filename: str):
    """
    Writes the certificate bytes to a file.
    
    Args:
        cert_bytes (bytes): The certificate's byte representation.
        filename (str): The output file name.
    """
    with open(filename, "wb") as f:
        f.write(cert_bytes)
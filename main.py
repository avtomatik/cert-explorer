import json
from pathlib import Path

from cryptography.hazmat.primitives import serialization

from cert_explorer.io import write_cert_to_file
from cert_explorer.parser import (
    get_certificate_info,
    parse_certificate_from_hex,
)


def main():
    PATH_SRC = Path("data")
    PATH_DST = Path("certificates")
    json_file = PATH_SRC / "dump.json"

    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    for i, entry in enumerate(data):
        raw_certificate = entry.get("RawCertificate")
        if not raw_certificate:
            print(f"Entry {i} has no RawCertificate field, skipping.")
            continue

        try:
            cert = parse_certificate_from_hex(raw_certificate)
            cert_info = get_certificate_info(cert)

            for key, value in cert_info.items():
                print(f"{key}: {value}")

            PATH_DST.mkdir(parents=True, exist_ok=True)
            file_path = PATH_DST / f"cert_{i:06}.der"
            write_cert_to_file(
                cert.public_bytes(encoding=serialization.Encoding.DER),
                file_path,
            )
            print(f"Saved certificate to {file_path}")

        except Exception as e:
            print(f"Failed to process certificate {i}: {e}.")


if __name__ == "__main__":
    main()

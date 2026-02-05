from cert_explorer.io import write_cert_to_file
from cert_explorer.parser import (
    get_certificate_info,
    parse_certificate_from_hex,
)


def main():
    raw_certificate = "0xabcdef"

    cert = parse_certificate_from_hex(raw_certificate)

    cert_info = get_certificate_info(cert)
    for key, value in cert_info.items():
        print(f"{key}: {value}")

    write_cert_to_file(cert.public_bytes(), "cert.der")


if __name__ == "__main__":
    main()

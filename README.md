# CertExplorer

CertExplorer is a small, modular Python tool for **processing raw hexadecimal X.509 certificates** at scale.

It reads certificates from a JSON dump, parses each raw hex certificate, prints key metadata, and writes each certificate to disk in **DER format** using **atomic file writes**.

The codebase is structured around **SOLID principles**, uses `typing.Protocol` instead of ABCs, and processes each certificate **independently and safely**.

---

## Project Structure

```
.
├── core
│   ├── interfaces.py   # Protocol definitions (Source / Writer)
│   ├── io.py           # Concrete I/O implementations
│   ├── parser.py       # Certificate parsing & inspection
│   └── processor.py   # Atomic certificate processing logic
├── data
│   └── .gitkeep        # JSON input directory (ignored by git)
├── main.py             # Application entry point
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Requirements

* Python 3.10+
* [`uv`](https://github.com/astral-sh/uv)
* `cryptography`

Dependencies are managed via **uv**, not `pip`.

---

## Installation

Sync the environment using `uv`:

```bash
uv sync
```

This will create a virtual environment and install all dependencies declared in `pyproject.toml`.

---

## Input Format

CertExplorer expects a JSON file at:

```
data/dump.json
```

Example structure:

```json
[
  {
    "RawCertificate": "0x3082030a02820301..."
  },
  {
    "RawCertificate": "0x3082025f308201c7..."
  }
]
```

Each entry is processed **independently**.

---

## Usage

Run the main application with:

```bash
uv run python main.py
```

What happens:

* Reads certificates from `data/dump.json`
* Parses each `RawCertificate`
* Prints certificate metadata:

  * subject
  * issuer
  * validity window (UTC)
* Writes each certificate to:

  ```
  certificates/cert_000000.der
  certificates/cert_000001.der
  ```
* Uses **atomic writes** to avoid partial or corrupt files
* Skips invalid entries without stopping the batch

---

## Design Notes

* **Atomic processing**: each certificate is processed in isolation
* **Atomic file writes**: temporary file → rename
* **SOLID architecture**:

  * `CertificateSource` and `CertificateWriter` are defined via `typing.Protocol`
  * Easy to add new input sources (DB, API) or outputs (ZIP, S3, etc.)
* **Test-friendly**: components are loosely coupled

---

## Contributing

Contributions are welcome!

Ideas for extensions:

* Alternative certificate sources (CSV, database, API)
* Additional output formats (PEM, ZIP bundles)
* Structured logging
* Metrics or reporting

Feel free to open an issue or submit a pull request.

---

import json
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable


class JSONCertificateSource:
    def __init__(self, json_path: Path):
        self.json_path = json_path

    def get_raw_certificates(self) -> Iterable[Dict[str, Any]]:
        with self.json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data


class FileCertificateWriter:
    """Writes certificates safely using temporary files for atomicity."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write_atomic(self, cert_bytes: bytes, name_hint: str) -> Path:
        final_path = self.output_dir / f"{name_hint}.der"
        # Write to a temporary file in the same directory first
        with tempfile.NamedTemporaryFile(
            dir=self.output_dir, delete=False, suffix=".der"
        ) as tmp_file:
            tmp_file.write(cert_bytes)
            tmp_file_path = Path(tmp_file.name)
        # Move temp file to final destination atomically
        tmp_file_path.replace(final_path)
        return final_path

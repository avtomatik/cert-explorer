from pathlib import Path
from typing import Any, Dict, Iterable, Protocol


class CertificateSource(Protocol):
    """Provides raw certificates as hex strings."""

    def get_raw_certificates(self) -> Iterable[Dict[str, Any]]: ...


class CertificateWriter(Protocol):
    """Writes certificate bytes to a destination."""

    def write_atomic(self, cert_bytes: bytes, name_hint: str) -> Path: ...

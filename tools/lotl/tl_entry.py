"""TL entry data model and parsing."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class TLEntry:
    """Represents a single TL entry from a participant JSON file."""

    tl_type: str
    participant_id: str
    tl_url: str
    tl_url_xml: Optional[str] = None
    tl_url_json: Optional[str] = None
    trust_anchor: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    source_path: Optional[Path] = None

    def get_tl_url_json(self) -> str:
        """Return JSON TL URL (tl_url_json or tl_url)."""
        return self.tl_url_json or self.tl_url

    def get_tl_url_xml(self) -> str:
        """Return XML TL URL (tl_url_xml or tl_url)."""
        return self.tl_url_xml or self.tl_url

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
        tl_type: str,
        participant_id: str,
        source_path: Optional[Path] = None,
    ) -> "TLEntry":
        """Create TLEntry from parsed JSON dict."""
        return cls(
            tl_type=tl_type,
            participant_id=participant_id,
            tl_url=data["tl_url"],
            tl_url_xml=data.get("tl_url_xml"),
            tl_url_json=data.get("tl_url_json"),
            trust_anchor=data.get("trust_anchor", ""),
            metadata=data.get("metadata", {}),
            source_path=source_path,
        )

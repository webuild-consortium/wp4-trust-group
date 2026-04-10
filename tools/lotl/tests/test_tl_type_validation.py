"""Tests for TL type validation."""

from tools.lotl.settings import VALID_TL_TYPES, TL_TYPE_TO_REFERENCE_URI


def test_valid_tl_types() -> None:
    """VALID_TL_TYPES contains expected types."""
    expected = {
        "wrpac-provider",
        "wrprc-provider",
        "pub-eaa-provider",
        "pid-provider",
        "qeaa-provider",
        "eaa-provider",
        "wallet-provider",
        "ebwoid-provider",
    }
    assert VALID_TL_TYPES == expected


def test_tl_type_to_reference_uri() -> None:
    """Each TL type maps to an ETSI LoTE type or TSL type URI."""
    for tl_type in VALID_TL_TYPES:
        assert tl_type in TL_TYPE_TO_REFERENCE_URI
        uri = TL_TYPE_TO_REFERENCE_URI[tl_type]
        assert uri.startswith("http://uri.etsi.org/")
    assert TL_TYPE_TO_REFERENCE_URI["qeaa-provider"].endswith("/EUgeneric")
    assert "LoTEType" in TL_TYPE_TO_REFERENCE_URI["eaa-provider"]


def test_get_schema_path() -> None:
    """get_schema_path returns valid path."""
    from tools.lotl.settings import get_schema_path

    path = get_schema_path()
    assert path.name == "tl_entry.json"
    assert path.exists()

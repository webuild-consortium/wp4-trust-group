"""Tests for package __init__."""

from tools.lotl import __version__


def test_version_defined() -> None:
    """__version__ is defined and non-empty."""
    assert __version__
    assert isinstance(__version__, str)

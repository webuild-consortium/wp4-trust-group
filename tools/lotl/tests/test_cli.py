"""Tests for CLI."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[3]  # wp4-trust-group root


def test_cli_validate_only(tmp_path: Path) -> None:
    """--validate-only runs without signing key."""
    import json

    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "x.json").write_text(
        json.dumps({
            "tl_url": "https://example.com/tl.json",
            "trust_anchor": "-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----",
        })
    )
    env = {**os.environ, "PYTHONPATH": str(PROJECT_ROOT)}
    result = subprocess.run(
        [sys.executable, "-m", "tools.lotl", "--validate-only", "--tl-entries-dir", str(tmp_path), "--output-dir", str(tmp_path)],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        env=env,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)


def test_cli_help() -> None:
    """--help works."""
    env = {**os.environ, "PYTHONPATH": str(PROJECT_ROOT)}
    result = subprocess.run(
        [sys.executable, "-m", "tools.lotl", "--help"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        env=env,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)
    assert "tl-entries-dir" in result.stdout


def test_cli_main_invocation(tl_entries_dir: Path) -> None:
    """CLI main() can be invoked directly."""
    from tools.lotl.cli import main

    exit_code = main([
        "--validate-only",
        "--tl-entries-dir", str(tl_entries_dir),
        "--output-dir", str(tl_entries_dir),
    ])
    assert exit_code == 0


def test_cli_inline_pem_path_nonexistent(tl_entries_dir: Path, signing_key_and_cert) -> None:
    """CLI with non-existent path returns path as-is (_load_pem_from_env_or_path fallback)."""
    from tools.lotl.cli import main

    _, cert_path = signing_key_and_cert
    # Non-existent path: p.exists() is False, returns path_arg (inline PEM path)
    exit_code = main([
        "--signing-key", "/nonexistent/key.pem",
        "--signing-cert", str(cert_path),
        "--tl-entries-dir", str(tl_entries_dir),
        "--output-dir", str(tl_entries_dir),
    ])
    assert exit_code != 0  # Produce fails with invalid key

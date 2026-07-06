"""Allow running as python -m tools.lotl."""

from tools.lotl.cli import main

if __name__ == "__main__":
    raise SystemExit(main())

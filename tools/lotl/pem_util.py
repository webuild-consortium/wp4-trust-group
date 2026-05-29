"""Normalize PEM material from CI secrets (e.g. GitHub Actions env)."""


def normalize_pem_for_ci(raw: str) -> str:
    """Turn PEM strings from CI env vars into parseable PEM.

    GitHub Secrets and similar stores often keep PEM as one line with literal
    ``\\n`` sequences, or with Windows newlines. Cryptography rejects that as
    MalformedFraming when loading PEM.
    """
    s = raw.strip().lstrip("\ufeff")
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1].strip()
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    if "-----BEGIN" in s and "\\n" in s:
        s = s.replace("\\n", "\n")
    return s

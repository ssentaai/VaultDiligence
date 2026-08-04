#!/usr/bin/env python3
"""Pre-commit secret scanner (Fix 42).

Scans staged files for accidentally committed secrets. Blocks the commit
(exit 1) if any pattern matches. The repo is public on GitHub, so this is the
last line of defence against leaking API keys, Ethereum private keys, or .env
content.

SECURITY INVARIANT: this script never prints matched secret text. It prints only
`path:line  PATTERN_NAME`. Logging the secret would defeat the purpose.

Usage:
  pre-commit-secret-scan.py                 # scan git-staged files (hook mode)
  pre-commit-secret-scan.py FILE [FILE...]  # scan explicit paths (test mode)

Bypass for legitimate cases:
  git commit --no-verify
  or add a line containing `secret-scan: allow` to the file (whole-file skip),
  or name the file *.env.example.

Exit codes: 0 = clean, 1 = secret(s) found, 2 = usage / git error.
"""

import re
import subprocess
import sys
from pathlib import Path

# --- Patterns (named; intent documented in docs/security-scans/pre-commit-setup.md) ---
# Each value is a compiled regex; the key is the NAME reported on a hit.
PATTERNS = {
    "GENERIC_API_KEY": re.compile(
        r"(api[_-]?key|api[_-]?token|secret|password|bearer)[=:][\s'\"]*[A-Za-z0-9_\-]{20,}",
        re.IGNORECASE,
    ),
    "ANTHROPIC_KEY": re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}"),
    "OPENAI_KEY": re.compile(r"sk-(?:proj-)?[A-Za-z0-9]{20,}"),
    # Exactly 64 hex chars after 0x, on a word boundary, to avoid matching
    # arbitrary long hex (e.g. tx hashes are 64 too — accepted false-positive
    # surface; bypass with the allow marker for documented example keys).
    "ETH_PRIVATE_KEY": re.compile(r"0x[0-9a-fA-F]{64}\b"),
    # .env-shaped line: UPPER_SNAKE key, '=' with no surrounding spaces, and a
    # token-like value (8+ non-space chars). Anchored, so prose like "NOTE = x"
    # and trivial "X=1" do not match. Suppressed in .env / .env.example files.
    "DOTENV_LINE": re.compile(r"^[A-Z][A-Z0-9_]+=\S{8,}$"),
    "AWS_ACCESS_KEY": re.compile(r"AKIA[0-9A-Z]{16}"),
}

# Whole-file allowlist: paths (posix form) that legitimately contain example
# secrets or the patterns themselves. Compared by suffix match.
ALLOWLISTED_SUFFIXES = (
    "scripts/pre-commit-secret-scan.py",       # this scanner (contains the patterns)
    "docs/security-scans/pre-commit-setup.md",  # setup doc (shows fake examples)
)

ALLOW_MARKER = "secret-scan: allow"  # any line containing this -> whole file skipped
MAX_BYTES = 2_000_000  # skip very large files; secrets live in small text files


def is_allowlisted_path(path: str) -> bool:
    p = path.replace("\\", "/")
    if p.endswith(".env.example"):
        return True
    return any(p.endswith(s) for s in ALLOWLISTED_SUFFIXES)


def staged_files() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"],
            capture_output=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"secret-scan: could not list staged files: {exc}", file=sys.stderr)
        sys.exit(2)
    return [f for f in out.decode("utf-8", "replace").split("\0") if f]


def read_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_BYTES:
            return None
        raw = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in raw:  # binary
        return None
    return raw.decode("utf-8", "replace")


def scan_file(path_str: str) -> list[tuple[int, str]]:
    """Return list of (line_number, pattern_name) hits. Never returns the text."""
    if is_allowlisted_path(path_str):
        return []
    path = Path(path_str)
    if not path.is_file():
        return []
    text = read_text(path)
    if text is None:
        return []
    if ALLOW_MARKER in text:  # explicit per-file opt-out
        return []

    is_envfile = path.name in (".env", ".env.example") or path.name.endswith(".env")
    hits: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for name, rx in PATTERNS.items():
            if name == "DOTENV_LINE" and is_envfile:
                continue
            if rx.search(line):
                hits.append((lineno, name))
    return hits


def main(argv: list[str]) -> int:
    files = argv[1:] if len(argv) > 1 else staged_files()
    findings: list[tuple[str, int, str]] = []
    for f in files:
        for lineno, name in scan_file(f):
            findings.append((f, lineno, name))

    if not findings:
        return 0

    print("\nsecret-scan: potential secrets detected in staged files\n", file=sys.stderr)
    for f, lineno, name in findings:
        print(f"  {f}:{lineno}  {name}", file=sys.stderr)  # NO matched text, ever
    print(
        "\nCommit blocked. If a match is a false positive or a documented example:\n"
        "  - add a line containing 'secret-scan: allow' to the file, or\n"
        "  - rename example files to *.env.example, or\n"
        "  - bypass once with: git commit --no-verify\n",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Generate a deterministic public catalog from knowledge Markdown files."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
OUTPUT = ROOT / "CATALOG.md"


def title_for(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return match.group(1).strip() if match else path.stem.replace("_", " ")


def main() -> None:
    files = sorted(KNOWLEDGE.rglob("*.md"), key=lambda p: p.as_posix().casefold())
    groups: dict[str, list[Path]] = {}
    for path in files:
        rel = path.relative_to(KNOWLEDGE)
        section = rel.parts[0] if len(rel.parts) > 1 else "Root"
        groups.setdefault(section, []).append(path)

    lines = [
        "# Knowledge Catalog",
        "",
        f"> Generated from {len(files)} public Markdown notes. Run `python scripts/generate_catalog.py` after adding or renaming notes.",
        "",
    ]
    for section in sorted(groups, key=str.casefold):
        lines.extend([f"## {section}", ""])
        for path in groups[section]:
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"- [{title_for(path)}]({rel})")
        lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

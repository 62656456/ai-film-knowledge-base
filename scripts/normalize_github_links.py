#!/usr/bin/env python3
"""Convert Obsidian links and normalize local Markdown links for GitHub."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
WIKILINK = re.compile(r"(!?)\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]")
INLINE_LINK = re.compile(r"(!?\[[^\]]*\])\((?!<)([^)\n]+)\)")
TITLE = re.compile(r"(?m)^#\s+(.+?)\s*$")


def github_fragment(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[\s]+", "-", value)
    value = re.sub(r"[`~!@#$%^&*()+=\[\]{}\\|;:'\",.<>/?，。；：！？（）【】《》]", "", value)
    return value


def markdown_destination(value: str) -> str:
    """Use CommonMark's angle-bracket form when a local target contains spaces."""
    return f"<{value}>" if any(character.isspace() for character in value) else value


def build_index(files: list[Path]) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    for path in files:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        title_match = TITLE.search(text)
        keys = {path.stem.casefold()}
        if title_match:
            keys.add(title_match.group(1).strip().casefold())
        for key in keys:
            index.setdefault(key, []).append(path)
    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Rewrite files after a clean dry run")
    args = parser.parse_args()

    knowledge_files = sorted(KNOWLEDGE.rglob("*.md"))
    repository_files = sorted(
        path for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and not path.name.endswith(".next.md")
    )
    index = build_index(knowledge_files)
    unresolved: list[str] = []
    ambiguous: list[str] = []
    changed: dict[Path, str] = {}
    converted = 0
    destinations_normalized = 0

    for path in repository_files:
        original = path.read_text(encoding="utf-8-sig", errors="replace")

        def replace_wikilink(match: re.Match[str]) -> str:
            nonlocal converted
            if not path.is_relative_to(KNOWLEDGE):
                return match.group(0)
            embed, raw_target, heading, label = match.groups()
            target = raw_target.strip()
            candidates = index.get(Path(target).name.casefold(), [])
            if not candidates:
                unresolved.append(f"{path.relative_to(ROOT)} -> {match.group(0)}")
                return match.group(0)
            if len(candidates) > 1:
                ambiguous.append(f"{path.relative_to(ROOT)} -> {match.group(0)}")
                return match.group(0)
            destination = candidates[0]
            relative = Path(os.path.relpath(destination, path.parent)).as_posix()
            if heading:
                relative += "#" + github_fragment(heading)
            visible = (label or heading or target).strip()
            converted += 1
            return f"{embed}[{visible}]({markdown_destination(relative)})"

        def normalize_destination(match: re.Match[str]) -> str:
            nonlocal destinations_normalized
            label, raw_target = match.groups()
            target = raw_target.strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                return match.group(0)
            if not any(character.isspace() for character in target):
                return match.group(0)
            destinations_normalized += 1
            return f"{label}(<{target}>)"

        updated = WIKILINK.sub(replace_wikilink, original)
        updated = INLINE_LINK.sub(normalize_destination, updated)
        if updated != original:
            changed[path] = updated

    print(f"Knowledge Markdown files indexed: {len(knowledge_files)}")
    print(f"Repository Markdown files checked: {len(repository_files)}")
    print(f"Wikilinks convertible: {converted}")
    print(f"Local destinations normalized: {destinations_normalized}")
    print(f"Files to change: {len(changed)}")
    print(f"Unresolved: {len(unresolved)}")
    for item in unresolved:
        print(f"UNRESOLVED: {item}")
    print(f"Ambiguous: {len(ambiguous)}")
    for item in ambiguous:
        print(f"AMBIGUOUS: {item}")

    if unresolved or ambiguous:
        return 1
    if args.write:
        for path, text in changed.items():
            path.write_text(text, encoding="utf-8", newline="\n")
        print(f"Rewritten: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the sanitized public theory-and-practice knowledge repository."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
EXPECTED_LAYERS = {"00-总纲", "A-理论层", "B-实战层"}
EXPECTED_COUNTS = {"00-总纲": 4, "A-理论层": 51, "B-实战层": 43}
EXPECTED_NOTES = 98
EXPECTED_IMAGE_NOTICES = 730
FORBIDDEN_LAYER_NAMES = {"C-AI基础设施", "D-复盘与验证层", "E-灵感参照层"}
FORBIDDEN_KNOWLEDGE_TERMS = ("00-04 新旧ID对照表", "project_005_SUPER_I_COURSE_KB")
PUBLIC_EMAIL = "haldissita@gmail.com"
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}"),
    "GitHub fine-grained token": re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9_-]{24,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
IMAGE_EMBED = re.compile(r"!\[[^\]]*\]\((?!https?://)[^)]+\)|!\[\[[^\]]+\]\]")
IMAGE_NOTICE = re.compile(r"Image omitted from the public edition")
PRIVATE_WINDOWS_PATH = re.compile(
    r"(?i)(?:[A-Z]:\\(?:Codex|zhishiku|Claude cold)\\|C:/Users/)[^\s`\"'<>]+"
)
EMAIL = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    markdown_files = sorted(KNOWLEDGE.rglob("*.md")) if KNOWLEDGE.exists() else []
    all_files = sorted(path for path in KNOWLEDGE.rglob("*") if path.is_file()) if KNOWLEDGE.exists() else []

    if not KNOWLEDGE.is_dir():
        errors.append("missing knowledge directory")
    layers = {path.name for path in KNOWLEDGE.iterdir() if path.is_dir()} if KNOWLEDGE.exists() else set()
    if layers != EXPECTED_LAYERS:
        errors.append(f"public layers must be {sorted(EXPECTED_LAYERS)}, found {sorted(layers)}")
    if layers & FORBIDDEN_LAYER_NAMES:
        errors.append("a private knowledge layer is present")
    if len(markdown_files) != EXPECTED_NOTES:
        errors.append(f"expected {EXPECTED_NOTES} Markdown notes, found {len(markdown_files)}")

    for layer, expected in EXPECTED_COUNTS.items():
        actual = len(list((KNOWLEDGE / layer).rglob("*.md"))) if (KNOWLEDGE / layer).exists() else 0
        if actual != expected:
            errors.append(f"{layer}: expected {expected} notes, found {actual}")

    non_markdown = [path for path in all_files if path.suffix.lower() != ".md"]
    for path in non_markdown:
        errors.append(f"non-Markdown file in public knowledge corpus: {path.relative_to(ROOT)}")

    notice_count = 0
    allowed_examples = {"test@example.com", "user@example.com", "name@example.com", PUBLIC_EMAIL}
    for path in markdown_files:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        notice_count += len(IMAGE_NOTICE.findall(text))
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label}: {path.relative_to(ROOT)}")
        if IMAGE_EMBED.search(text):
            errors.append(f"local image embed remains: {path.relative_to(ROOT)}")
        if PRIVATE_WINDOWS_PATH.search(text):
            errors.append(f"local absolute path reference: {path.relative_to(ROOT)}")
        for term in FORBIDDEN_KNOWLEDGE_TERMS:
            if term in text:
                errors.append(f"forbidden private/history reference in {path.relative_to(ROOT)}: {term}")
        for match in EMAIL.finditer(text):
            if match.group(0).lower() not in allowed_examples:
                errors.append(f"unapproved email address: {path.relative_to(ROOT)}")

    if notice_count != EXPECTED_IMAGE_NOTICES:
        errors.append(
            f"expected {EXPECTED_IMAGE_NOTICES} public image notices, found {notice_count}"
        )

    generator = ROOT / "scripts" / "generate_catalog.py"
    subprocess.run([sys.executable, str(generator)], check=True)
    catalog = ROOT / "CATALOG.md"
    if not catalog.exists():
        errors.append("catalog generation failed")
    else:
        catalog_text = catalog.read_text(encoding="utf-8-sig")
        if f"Generated from {EXPECTED_NOTES} public Markdown notes" not in catalog_text:
            errors.append("catalog note count is stale")

    print(f"Knowledge notes checked: {len(markdown_files)}")
    for layer in sorted(EXPECTED_LAYERS):
        print(f"{layer}: {len(list((KNOWLEDGE / layer).rglob('*.md')))}")
    print(f"Public image notices checked: {notice_count}")
    print(f"Other files under knowledge/: {len(non_markdown)}")
    print(f"Warnings: {len(warnings)}")
    for warning in sorted(set(warnings)):
        print(f"WARN: {warning}")
    print(f"Errors: {len(errors)}")
    for error in sorted(set(errors)):
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

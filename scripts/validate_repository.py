#!/usr/bin/env python3
"""Validate the public GitHub-reading edition of the AI Film Knowledge Base."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
VISUAL_DIR = ROOT / "docs" / "assets" / "knowledge"
VISUAL_REGISTER = ROOT / "docs" / "VISUAL_ASSETS.md"

EXPECTED_LAYERS = {
    "00-总纲",
    "A-理论层",
    "B-实战层",
    "C-审核与验收层",
}
EXPECTED_COUNTS = {
    "00-总纲": 4,
    "A-理论层": 51,
    "B-实战层": 43,
    "C-审核与验收层": 7,
}
EXPECTED_NOTES = 105
FORBIDDEN_LAYER_NAMES = {
    "C-AI基础设施",
    "D-复盘与验证层",
    "E-灵感参照层",
}
FORBIDDEN_KNOWLEDGE_TERMS = {
    "00-04 新旧ID对照表",
    "project_005_SUPER_I_COURSE_KB",
    "session_meta.payload.id",
    "archived_sessions",
}
FORBIDDEN_PERSONAL_PROJECT_TERMS = {
    "石猴·阿隙",
    "狼人短剧",
    "山海镇妖录",
    "《最后同步》",
    "《女孩和狗》",
}

PUBLIC_EMAIL = "haldissita@gmail.com"
ALLOWED_EMAILS = {
    "test@example.com",
    "user@example.com",
    "name@example.com",
    PUBLIC_EMAIL,
}

EXPECTED_VISUAL_ALTS = {
    "knowledge-route.svg": (
        "Choose A Theory, B Practice, or C Review directly on GitHub; "
        "every route remains independently usable."
    ),
    "shot-scale-ladder.svg": "人物在八种景别中的画面占比递进示意",
    "camera-coordinate-system.svg": "摄影机高度、俯仰、横滚与方位角坐标示意",
    "blocking-dual-channel.svg": "人物世界坐标与摄影机画面投影的双通道调度示意",
    "story-pressure-chain.svg": "六节点剧情压力链从缺口到不可逆选择的递进示意",
    "prompt-four-step.svg": "提示词从意图、拆解、组装到审核退回的四步流程",
    "evidence-ladder.svg": "结构、内容、真实结果与审核接受的证据等级阶梯",
    "review-return-loop.svg": "审核失败后退回最早断裂决策并重新验证的闭环",
    "five-gate-film-check.svg": "AI影视成品的故事、连续性、视觉、时间声音与交付五门验收",
    "public-image-gate.svg": "公开图片从作者、隐私、用途、登记到发布的五项过闸流程",
}

REQUIRED_DOCUMENT_TEXT = {
    "README.md": (
        "105 authored Markdown notes",
        "622 conditional candidates",
        "86 files",
        "22 files",
        "knowledge/C-审核与验收层/",
        "docs/VISUAL_ASSETS.md",
    ),
    "docs/i18n/zh-CN/README.md": (
        "105 篇 Markdown",
        "622 张条件候选",
        "86 张",
        "22 张",
    ),
    "docs/i18n/ja/README.md": (
        "105件のMarkdown",
        "622点",
        "86点",
        "22点",
    ),
    "docs/i18n/ko/README.md": (
        "105개의 Markdown",
        "622개",
        "86개",
        "22개",
    ),
    "PUBLICATION_SCOPE.md": (
        "105 personally authored Markdown notes",
        "Conditional candidates",
        "| 622 |",
        "| 86 |",
        "| 22 |",
        "| 0 |",
    ),
    "llms.txt": (
        "Public corpus: 105 Markdown notes.",
        "knowledge/C-审核与验收层/",
        "622 remain private conditional candidates",
    ),
}

SECRET_PATTERNS = {
    "GitHub token": re.compile(r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}"),
    "GitHub fine-grained token": re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9_-]{24,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private key block": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    ),
}

MARKDOWN_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\r\n]+)\)")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\r\n]+)\)")
HTML_IMAGE = re.compile(r"<img\b([^>]+)>", re.IGNORECASE)
HTML_ATTRIBUTE = re.compile(
    r"\b(src|alt)\s*=\s*([\"'])(.*?)\2", re.IGNORECASE | re.DOTALL
)
WIKILINK = re.compile(r"!?\[\[[^\]]+\]\]")
LEGACY_IMAGE_NOTICE = re.compile(
    r"Image omitted from the public edition", re.IGNORECASE
)
PRIVATE_WINDOWS_PATH = re.compile(
    r"(?i)(?:\b[A-Z]:[\\/]|C:/Users/|\\\\[^\\\s]+\\)"
)
SESSION_UUID = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-"
    r"[0-9a-f]{4}-[0-9a-f]{12}\b",
    re.IGNORECASE,
)
PRIVATE_REVIEW_ID = re.compile(r"\bD1-\d{2}\b")
EMAIL = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
FENCED_CODE = re.compile(
    r"(?ms)^[ \t]*(?:\x60{3}|~~~).*?^[ \t]*(?:\x60{3}|~~~)[ \t]*$"
)
GENERIC_ALT = re.compile(
    r"(?i)^(?:image|img|diagram|figure|graphic|photo|picture|svg|图片|图|示意图)$"
)
REMOTE_TARGET = re.compile(r"(?i)^(?:https?://|mailto:|data:|//)")
UNSAFE_SVG = re.compile(
    r"(?i)<script\b|javascript:|<foreignObject\b|<image\b|"
    r"(?:href|xlink:href)\s*=\s*[\"'](?:https?:|//|data:)"
)


def strip_fenced_code(text: str) -> str:
    return FENCED_CODE.sub("", text)


def clean_target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        value = value[1 : value.index(">")]
    else:
        titled = re.match(r"^(.*?)(?:\s+[\"'][^\"']*[\"'])$", value)
        if titled:
            value = titled.group(1).strip()
    return unquote(value)


def resolve_local_target(source: Path, raw_target: str) -> tuple[Path | None, str | None]:
    target = clean_target(raw_target)
    if not target or target.startswith("#") or REMOTE_TARGET.match(target):
        return None, None
    file_target = target.split("#", 1)[0].split("?", 1)[0]
    if not file_target:
        return None, None
    if file_target.startswith("/"):
        return None, "repository-relative links must not start with /"
    resolved = (source.parent / file_target).resolve()
    try:
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        return None, "local link escapes the repository"
    return resolved, None


def is_under(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def public_markdown_files() -> list[Path]:
    files = {
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "_temp" not in path.parts
    }
    return sorted(files, key=lambda path: path.as_posix().casefold())


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not KNOWLEDGE.is_dir():
        errors.append("missing knowledge directory")
        markdown_files: list[Path] = []
        all_knowledge_files: list[Path] = []
        layers: set[str] = set()
    else:
        markdown_files = sorted(KNOWLEDGE.rglob("*.md"))
        all_knowledge_files = sorted(
            path for path in KNOWLEDGE.rglob("*") if path.is_file()
        )
        layers = {path.name for path in KNOWLEDGE.iterdir() if path.is_dir()}

    if layers != EXPECTED_LAYERS:
        errors.append(
            f"public layers must be {sorted(EXPECTED_LAYERS)}, found {sorted(layers)}"
        )
    if layers & FORBIDDEN_LAYER_NAMES:
        errors.append("a private knowledge layer is present")
    if len(markdown_files) != EXPECTED_NOTES:
        errors.append(
            f"expected {EXPECTED_NOTES} Markdown notes, found {len(markdown_files)}"
        )

    for layer, expected in EXPECTED_COUNTS.items():
        layer_path = KNOWLEDGE / layer
        actual = len(list(layer_path.rglob("*.md"))) if layer_path.exists() else 0
        if actual != expected:
            errors.append(f"{layer}: expected {expected} notes, found {actual}")

    non_markdown = [
        path for path in all_knowledge_files if path.suffix.lower() != ".md"
    ]
    for path in non_markdown:
        errors.append(
            f"non-Markdown file in public knowledge corpus: {path.relative_to(ROOT)}"
        )

    generator = ROOT / "scripts" / "generate_catalog.py"
    catalog = ROOT / "CATALOG.md"
    catalog_before = (
        catalog.read_text(encoding="utf-8-sig", errors="replace")
        if catalog.exists()
        else None
    )
    try:
        subprocess.run([sys.executable, str(generator)], check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"catalog generation failed: {exc}")
    catalog_after = (
        catalog.read_text(encoding="utf-8-sig", errors="replace")
        if catalog.exists()
        else None
    )
    if catalog_after is None:
        errors.append("catalog generation did not produce CATALOG.md")
    else:
        if f"Generated from {EXPECTED_NOTES} public Markdown notes" not in catalog_after:
            errors.append("catalog note count is stale")
        if "## C-审核与验收层" not in catalog_after:
            errors.append("catalog is missing the public C review layer")
        if catalog_before != catalog_after:
            errors.append("CATALOG.md was stale and has been regenerated")

    for relative, required_strings in REQUIRED_DOCUMENT_TEXT.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required public document: {relative}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for required in required_strings:
            if required not in text:
                errors.append(f"{relative}: missing required public fact: {required}")

    actual_visual_files = (
        {path.name for path in VISUAL_DIR.iterdir() if path.is_file()}
        if VISUAL_DIR.is_dir()
        else set()
    )
    expected_visual_files = set(EXPECTED_VISUAL_ALTS)
    if actual_visual_files != expected_visual_files:
        errors.append(
            "registered visual file set mismatch: "
            f"expected {sorted(expected_visual_files)}, "
            f"found {sorted(actual_visual_files)}"
        )

    register_text = (
        VISUAL_REGISTER.read_text(encoding="utf-8-sig", errors="replace")
        if VISUAL_REGISTER.is_file()
        else ""
    )
    if not register_text:
        errors.append("missing or empty docs/VISUAL_ASSETS.md")
    registered_alts = dict(
        re.findall(
            r"^\| `docs/assets/knowledge/([A-Za-z0-9._-]+\.svg)` "
            r"\| `([^`]+)` \|",
            register_text,
            re.MULTILINE,
        )
    )
    registered_names = set(registered_alts)
    if registered_names != expected_visual_files:
        errors.append(
            "visual register mismatch: "
            f"expected {sorted(expected_visual_files)}, "
            f"found {sorted(registered_names)}"
        )
    if registered_alts != EXPECTED_VISUAL_ALTS:
        errors.append("visual register exact-alt allowlist does not match v1.1.0 contract")
    for heading in (
        "Exact alternative text",
        "Knowledge purpose",
        "Embedded in",
        "Author / rights basis",
        "Review status",
    ):
        if heading not in register_text:
            errors.append(f"visual register is missing field: {heading}")

    for name in sorted(actual_visual_files):
        path = VISUAL_DIR / name
        if path.suffix.lower() != ".svg":
            errors.append(f"knowledge visual is not SVG: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if "<svg" not in text or "xmlns=" not in text:
            errors.append(f"invalid SVG root: {path.relative_to(ROOT)}")
        if UNSAFE_SVG.search(text):
            errors.append(f"unsafe or externally dependent SVG: {path.relative_to(ROOT)}")
        if PRIVATE_WINDOWS_PATH.search(text) or SESSION_UUID.search(text):
            errors.append(f"private metadata in SVG: {path.relative_to(ROOT)}")

    visual_references = {name: 0 for name in registered_alts}
    local_links_checked = 0
    local_images_checked = 0
    wikilink_locations: list[str] = []
    legacy_notice_count = 0
    legacy_notice_files: set[str] = set()

    markdown_public = public_markdown_files()
    sensitive_public_files = markdown_public + [ROOT / "llms.txt"]

    for path in sensitive_public_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        relative = path.relative_to(ROOT)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label}: {relative}")
        if PRIVATE_WINDOWS_PATH.search(text):
            errors.append(f"local absolute path reference: {relative}")
        if SESSION_UUID.search(text):
            errors.append(f"session or conversation UUID: {relative}")
        if PRIVATE_REVIEW_ID.search(text):
            errors.append(f"private review-card identifier: {relative}")
        for match in EMAIL.finditer(text):
            if match.group(0).lower() not in ALLOWED_EMAILS:
                errors.append(f"unapproved email address: {relative}")
        for term in FORBIDDEN_PERSONAL_PROJECT_TERMS:
            if term in text:
                errors.append(f"personal project reference in {relative}: {term}")

    for path in markdown_files:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        relative = path.relative_to(ROOT)
        for term in FORBIDDEN_KNOWLEDGE_TERMS:
            if term in text:
                errors.append(f"forbidden private/history reference in {relative}: {term}")
        for layer_name in FORBIDDEN_LAYER_NAMES:
            if layer_name in text:
                errors.append(f"private layer reference in public knowledge: {relative}")

    for path in markdown_public:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        relative = path.relative_to(ROOT)
        visible_text = strip_fenced_code(text)

        found_wikilinks = WIKILINK.findall(visible_text)
        if found_wikilinks:
            wikilink_locations.append(
                f"{relative}: {len(found_wikilinks)} wikilink(s)"
            )

        notice_matches = LEGACY_IMAGE_NOTICE.findall(text)
        if notice_matches:
            legacy_notice_count += len(notice_matches)
            legacy_notice_files.add(str(relative))

        for match in MARKDOWN_LINK.finditer(visible_text):
            resolved, problem = resolve_local_target(path, match.group(1))
            if problem:
                errors.append(f"{relative}: {problem}: {match.group(1)}")
            elif resolved is not None:
                local_links_checked += 1
                if not resolved.exists():
                    errors.append(
                        f"broken local Markdown link in {relative}: {match.group(1)}"
                    )

        image_records: list[tuple[str, str, str]] = []
        for match in MARKDOWN_IMAGE.finditer(visible_text):
            image_records.append(("Markdown", match.group(1).strip(), match.group(2)))

        for match in HTML_IMAGE.finditer(visible_text):
            attributes = {
                name.lower(): value
                for name, _, value in HTML_ATTRIBUTE.findall(match.group(1))
            }
            if "src" not in attributes:
                errors.append(f"HTML image without src: {relative}")
                continue
            image_records.append(
                ("HTML", attributes.get("alt", "").strip(), attributes["src"])
            )

        for syntax, alt, raw_target in image_records:
            target = clean_target(raw_target)
            external = bool(REMOTE_TARGET.match(target))
            if is_under(path, KNOWLEDGE) and external:
                errors.append(
                    f"external image embed in public knowledge: {relative}: {target}"
                )
                continue
            if external:
                continue
            resolved, problem = resolve_local_target(path, raw_target)
            if problem:
                errors.append(f"{relative}: {problem}: {raw_target}")
                continue
            if resolved is None:
                continue
            local_images_checked += 1
            if not resolved.is_file():
                errors.append(f"broken local image in {relative}: {raw_target}")
                continue
            if not alt or GENERIC_ALT.fullmatch(alt):
                errors.append(
                    f"missing or generic image alt in {relative}: {raw_target}"
                )

            if is_under(resolved, VISUAL_DIR):
                name = resolved.name
                if name not in registered_alts:
                    errors.append(
                        f"unregistered knowledge visual in {relative}: {raw_target}"
                    )
                    continue
                visual_references[name] += 1
                expected_alt = registered_alts[name]
                if alt != expected_alt:
                    errors.append(
                        f"incorrect alt for {name} in {relative}: "
                        f"expected {expected_alt!r}, found {alt!r}"
                    )
            elif is_under(path, KNOWLEDGE):
                errors.append(
                    f"knowledge image is outside registered visual directory: "
                    f"{relative}: {raw_target}"
                )

    if wikilink_locations:
        sample = "; ".join(wikilink_locations[:5])
        errors.append(
            f"Obsidian wikilinks remain in public Markdown: "
            f"{len(wikilink_locations)} file(s); {sample}"
        )
    if legacy_notice_count:
        errors.append(
            "legacy public-image placeholders remain: "
            f"{legacy_notice_count} occurrence(s) in "
            f"{len(legacy_notice_files)} file(s)"
        )

    unreferenced_visuals = [
        name for name, count in visual_references.items() if count == 0
    ]
    if unreferenced_visuals:
        errors.append(
            f"registered visuals not referenced from Markdown: "
            f"{sorted(unreferenced_visuals)}"
        )

    print(f"Knowledge notes checked: {len(markdown_files)}")
    for layer in sorted(EXPECTED_LAYERS):
        layer_path = KNOWLEDGE / layer
        actual = len(list(layer_path.rglob("*.md"))) if layer_path.exists() else 0
        print(f"{layer}: {actual}")
    print(f"Knowledge directory non-Markdown files: {len(non_markdown)}")
    print(f"Registered original SVGs checked: {len(actual_visual_files)}")
    print(
        "Referenced registered SVGs: "
        f"{sum(1 for count in visual_references.values() if count > 0)}"
    )
    print(f"Local image embeds checked: {local_images_checked}")
    print(f"Local Markdown links checked: {local_links_checked}")
    print(f"Legacy image placeholders: {legacy_notice_count}")
    print(f"Obsidian wikilink files: {len(wikilink_locations)}")
    print(f"Warnings: {len(warnings)}")
    for warning in sorted(set(warnings)):
        print(f"WARN: {warning}")
    print(f"Errors: {len(set(errors))}")
    for error in sorted(set(errors)):
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

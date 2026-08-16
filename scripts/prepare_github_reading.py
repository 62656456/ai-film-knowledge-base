#!/usr/bin/env python3
"""Prepare the public knowledge notes for direct, uncluttered GitHub reading.

The source-vault images are intentionally not restored here. This script removes
the repetitive public-edition placeholder syntax, preserves descriptive image
ideas as text examples, prunes headings whose entire subtree became empty, adds
one rights note per affected teaching card, and embeds only the original public
SVGs registered in docs/VISUAL_ASSETS.md.
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
VISUAL_REGISTER = ROOT / "docs" / "VISUAL_ASSETS.md"

GENERIC_NOTICE = re.compile(
    r"^\s*>?\s*\[Image omitted from the public edition pending source and reuse-rights verification\.\]\s*$"
)
DESCRIPTIVE_NOTICE = re.compile(
    r"^\s*>?\s*\[Image omitted from the public edition:\s*(.+?)\.\s*"
    r"Source and reuse rights are pending verification\.\]\s*$"
)
MANIFEST_NOTICE = re.compile(
    r"^\s*-\s*\*\*正文嵌入\*\*：`\[Image omitted from the public edition pending source and reuse-rights verification\.\]`\s*$"
)
HEADING = re.compile(r"^(#{1,6})\s+\S")
PUBLIC_NOTE_MARKER = "> **公开图像说明：**"


@dataclass(frozen=True)
class PublicVisual:
    note: str
    anchor: str
    file: str
    alt: str


PUBLIC_VISUALS = (
    PublicVisual(
        "knowledge/A-理论层/A1-摄影组/A1-01 景别系统.md",
        "## 八级景别合同（统一记录字段）",
        "shot-scale-ladder.svg",
        "人物在八种景别中的画面占比递进示意",
    ),
    PublicVisual(
        "knowledge/A-理论层/A1-摄影组/A1-02 镜头角度系统.md",
        "### 机位方位罗盘",
        "camera-coordinate-system.svg",
        "摄影机高度、俯仰、横滚与方位角坐标示意",
    ),
    PublicVisual(
        "knowledge/A-理论层/A2-导演组/A2-01 调度与场面调度.md",
        "## AI分镜必须走“双通道”",
        "blocking-dual-channel.svg",
        "人物世界坐标与摄影机画面投影的双通道调度示意",
    ),
    PublicVisual(
        "knowledge/A-理论层/A3-编剧组/A3-10 结构压力链：六节点升级.md",
        "## 六节点压力链",
        "story-pressure-chain.svg",
        "六节点剧情压力链从缺口到不可逆选择的递进示意",
    ),
    PublicVisual(
        "knowledge/B-实战层/B2-提示词工程组/B2-02 四步工作流程.md",
        "## 四步流程总览",
        "prompt-four-step.svg",
        "提示词从意图、拆解、组装到审核退回的四步流程",
    ),
    PublicVisual(
        "knowledge/C-审核与验收层/C1-01 状态与证据等级.md",
        "## 先分开四类事实",
        "evidence-ladder.svg",
        "结构、内容、真实结果与审核接受的证据等级阶梯",
    ),
    PublicVisual(
        "knowledge/C-审核与验收层/C1-03 失败定位与定向退回.md",
        "# 失败定位与定向退回",
        "review-return-loop.svg",
        "审核失败后退回最早断裂决策并重新验证的闭环",
    ),
    PublicVisual(
        "knowledge/C-审核与验收层/C1-04 AI影视成品五门验收.md",
        "# AI影视成品五门验收",
        "five-gate-film-check.svg",
        "AI影视成品的故事、连续性、视觉、时间声音与交付五门验收",
    ),
    PublicVisual(
        "knowledge/C-审核与验收层/C1-06 知识与图片公开过闸.md",
        "# 知识与图片公开过闸",
        "public-image-gate.svg",
        "公开图片从作者、隐私、用途、登记到发布的五项过闸流程",
    ),
)


def relative_link(source: Path, destination: Path) -> str:
    return Path(os.path.relpath(destination, source.parent)).as_posix()


def prune_empty_heading_subtrees(lines: list[str]) -> tuple[list[str], int]:
    """Remove headings whose complete section subtree has no meaningful content."""
    headings: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = HEADING.match(line)
        if match:
            headings.append((index, len(match.group(1))))

    remove: set[int] = set()
    for position, (start, level) in enumerate(headings):
        end = len(lines)
        for candidate, candidate_level in headings[position + 1 :]:
            if candidate_level <= level:
                end = candidate
                break
        meaningful = any(
            line.strip() and not HEADING.match(line)
            for line in lines[start + 1 : end]
        )
        if not meaningful:
            remove.add(start)

    result = [line for index, line in enumerate(lines) if index not in remove]
    return result, len(remove)


def collapse_blank_lines(lines: list[str]) -> list[str]:
    result: list[str] = []
    for line in lines:
        if not line.strip() and result and not result[-1].strip():
            continue
        result.append(line if line.strip() else "")
    while result and not result[-1].strip():
        result.pop()
    return result


def add_page_rights_note(path: Path, lines: list[str]) -> list[str]:
    if PUBLIC_NOTE_MARKER in "\n".join(lines) or "assets" in path.relative_to(KNOWLEDGE).parts:
        return lines
    register = relative_link(path, VISUAL_REGISTER)
    note = (
        f"{PUBLIC_NOTE_MARKER} 原资料中未完成再分发权核验的图片不进入公开仓库；"
        f"本页只显示已登记的原创公共图示。详见 [视觉资产登记]({register})。"
    )
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return [*lines[: index + 1], "", note, *lines[index + 1 :]]
    raise ValueError(f"teaching note has no H1: {path.relative_to(ROOT)}")


def clean_note(path: Path, text: str) -> tuple[str, dict[str, int]]:
    stats = {"generic": 0, "descriptive": 0, "manifest": 0, "headings": 0}
    output: list[str] = []
    affected = False
    for line in text.splitlines():
        descriptive = DESCRIPTIVE_NOTICE.match(line)
        if descriptive:
            description = descriptive.group(1).strip()
            punctuation = "" if description.endswith(("。", "！", "？", ".", "!", "?")) else "。"
            output.append(f"> **文字化视觉示例：** {description}{punctuation}")
            stats["descriptive"] += 1
            affected = True
            continue
        if GENERIC_NOTICE.match(line):
            stats["generic"] += 1
            affected = True
            continue
        if MANIFEST_NOTICE.match(line):
            output.append("- **公开版图像状态**：源图未进入公开仓库，正文不保留逐图占位。")
            stats["manifest"] += 1
            affected = True
            continue
        output.append(line)

    if not affected:
        return text, stats
    output, stats["headings"] = prune_empty_heading_subtrees(output)
    output = add_page_rights_note(path, output)
    output = collapse_blank_lines(output)
    return "\n".join(output) + "\n", stats


def embed_public_visual(visual: PublicVisual, write: bool) -> bool:
    path = ROOT / visual.note
    text = path.read_text(encoding="utf-8-sig")
    if visual.file in text:
        return False
    if text.count(visual.anchor) != 1:
        raise ValueError(f"expected one image anchor in {visual.note}: {visual.anchor!r}")
    source = ROOT / "docs" / "assets" / "knowledge" / visual.file
    if not source.is_file():
        raise FileNotFoundError(source)
    link = relative_link(path, source)
    image = f'<img src="{link}" width="100%" alt="{visual.alt}" />'
    text = text.replace(visual.anchor, f"{visual.anchor}\n\n{image}", 1)
    if write:
        path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the prepared Markdown files")
    args = parser.parse_args()

    totals = {"files": 0, "generic": 0, "descriptive": 0, "manifest": 0, "headings": 0}
    pending: list[tuple[Path, str]] = []
    for path in sorted(KNOWLEDGE.rglob("*.md")):
        text = path.read_text(encoding="utf-8-sig")
        cleaned, stats = clean_note(path, text)
        if cleaned != text:
            totals["files"] += 1
            for key in ("generic", "descriptive", "manifest", "headings"):
                totals[key] += stats[key]
            pending.append((path, cleaned))

    if args.write:
        for path, cleaned in pending:
            path.write_text(cleaned, encoding="utf-8", newline="\n")

    embedded = sum(1 for visual in PUBLIC_VISUALS if embed_public_visual(visual, args.write))
    mode = "written" if args.write else "dry-run"
    print(f"Mode: {mode}")
    print(f"Knowledge files changed: {totals['files']}")
    print(f"Generic notices removed: {totals['generic']}")
    print(f"Descriptive notices preserved as text: {totals['descriptive']}")
    print(f"Manifest notice rows normalized: {totals['manifest']}")
    print(f"Empty headings pruned: {totals['headings']}")
    print(f"Original public visuals embedded: {embedded}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

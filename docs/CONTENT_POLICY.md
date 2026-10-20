# Content policy

## Public content classes

- **Stable mechanism**: a film-language, story, directing, production, or review principle with an explained causal use and stated limits.
- **Source-backed interpretation**: an explanation derived from identified evidence without presenting interpretation as source fact.
- **Practical method**: a repeatable workflow with bounded inputs, outputs, return conditions, and checks.
- **Candidate method**: promising but not sufficiently validated; its status, missing evidence, and failure conditions must be explicit.
- **Time-sensitive fact**: product, platform, model, price, feature, specification, or policy information that requires current primary-source verification.
- **Review standard**: an observable gate that states what is inspected, what causes return, what evidence permits resubmission, and what counts as passing.

## Public knowledge structure

- Theory belongs under `knowledge/A-理论层/`.
- Practice belongs under `knowledge/B-实战层/`.
- Public review and acceptance methods belong under `knowledge/C-审核与验收层/`.
- Public navigation, policy, and errata belong under `knowledge/00-总纲/`.

The public C layer is newly authored, reusable guidance. It is not the private `C-AI基础设施` layer, the private `D-复盘与验证层`, or the private `E-灵感参照层`. Those private layers remain forbidden in the public corpus.

The `knowledge/` directory is Markdown-only. Images, scripts, application state, caches, and generated binaries do not belong inside it.

## GitHub direct-reading contract

Every public note must be understandable when opened directly in GitHub without a private vault, hidden project, local application, or companion Skill.

- State the note's purpose and intended use.
- Define required inputs, workflow, output, return conditions, and pass standard when the note is procedural.
- Use ordinary Markdown links whose local targets resolve inside the repository.
- Do not use Obsidian wikilinks or embeds.
- Do not leave rights-review placeholders, missing-image notices, or silent local-image links in public notes.
- Use an accurate, specific alternative text for every image; generic text such as `image`, `diagram`, or a filename does not pass.

## Public boundary

Do not publish personal identity, personal projects, project names or status, private retrospectives, private validation evidence, company or client work, unpublished assets, credentials, raw private chats, session or conversation identifiers, personal behavior analysis, local application state, machine-specific configuration, local absolute paths, or full copied third-party works.

The maintainer's deliberately published contact address `haldissita@gmail.com` is the sole contact-information exception.

Replacing a project name or deleting a person's name is not sufficient anonymization when dates, counts, quotes, story facts, asset states, or identifiers can reconstruct the private source. Rewrite the public principle from first principles and use a fictional example.

## Image publication gate

The existing public-note image set was expressly authorized for publication on 2026-10-20: 696 original teaching images with 730 placements, plus the existing ten public-method SVGs. The old blanket hold is superseded. Publishing an illustration does not mark it aesthetically accepted or validate a depicted method.

Every added image must have a stable repository file, a record in `IMAGE_MANIFEST.json` or `VISUAL_ASSETS.md`, meaningful alternative text, a knowledge use, a source/creation basis, a license or explicit permission, modification history, and public reading locations. Preserve original bytes when no edit was requested. Private account, project and personal data remain excluded.

Images stay outside `knowledge/`, and knowledge pages use ordinary relative embeds. Verify file existence, hashes, references and safe SVG content. Do not reintroduce a blanket no-image rule or an original-SVG-only rule. Real film frames and external reference photographs must retain their actual source and rights attribution; a generated illustration must not be labeled as an actual film frame.

## Review, return, and status

Keep structure, content, real-result, and reviewer-acceptance evidence separate. A file that exists or a validator that passes does not prove that the method, image, Skill, or finished media has been accepted.

When a contribution fails, the return record must identify the failed gate, observed evidence, earliest broken decision, minimum correction, protected passing items, and proof required for resubmission. Use explicit states such as candidate, in review, changes requested, approved, published, blocked, or deprecated; do not silently promote a candidate.

## Sources and translations

- Link to primary and authoritative sources when a claim may change over time.
- Mark dead or unreadable links instead of reconstructing their content from memory.
- Separate source fact, interpretation, practical experience, candidate method, and unknown.
- Keep the Simplified Chinese note canonical unless its status explicitly changes.
- Store translations separately and link them from the source; do not silently overwrite it.
- A translation may improve clarity but must not add factual claims without updating the source note and evidence.

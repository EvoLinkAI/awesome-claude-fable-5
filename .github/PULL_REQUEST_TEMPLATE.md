# Pull Request

## What changed?

Briefly describe what this PR adds or updates.

## Usecase submission

Fill this section when adding or changing a case.

- Case number:
- Original source link:
- Creator handle:
- Creator profile link:
- Evidence type: Demo / Tutorial / Evaluation / Integration / Benchmark / Limit
- Publication date: YYYY-MM-DD
- Primary topic:

## Case content checklist

- [ ] The case heading uses `### Case X: [Title](source-link)`.
- [ ] The case has a stable `<a id="case-x"></a>` anchor.
- [ ] The first line under the heading is a bold usage takeaway.
- [ ] The body explains what the creator actually used Claude Fable 5 for.
- [ ] Source-content notes are written as normal Markdown paragraphs, not a generic excerpt block.
- [ ] Code blocks are used only for actual code, prompts, commands, or structured examples.
- [ ] The case includes `Type: ... | Date: YYYY-MM-DD`.
- [ ] The creator is credited with a profile link.
- [ ] The Menu links to the new or updated case anchor.

## Do not include

- [ ] No `How to use it:` label.
- [ ] No `Tweet excerpt` label.
- [ ] No invented prompt, workflow, benchmark result, or creator attribution.
- [ ] No vague creator rollups such as "more creators" when named creators are available.
- [ ] No public per-case quality badge unless the repository format changes.

## Localization checklist

- [ ] `README.md` was updated first.
- [ ] `README_es.md` was synced.
- [ ] `README_pt.md` was synced.
- [ ] `README_ja.md` was synced.
- [ ] `README_ko.md` was synced.
- [ ] `README_de.md` was synced.
- [ ] `README_fr.md` was synced.
- [ ] `README_tr.md` was synced.
- [ ] `README_zh-TW.md` was synced.
- [ ] `README_zh-CN.md` was synced.
- [ ] `README_ru.md` was synced.

## Validation

Run the checks from [docs/maintenance.md](../docs/maintenance.md) before requesting review.

- [ ] Every README has the expected case count.
- [ ] Every README has matching `case-x` anchors.
- [ ] No broken banner path was introduced.
- [ ] No placeholder translation text remains.
- [ ] The curated dataset was updated when the case list changed.

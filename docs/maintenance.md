# Maintenance Notes

This repository is a curated usecase content repository. The public README files are manually edited source-of-truth documents, not generated build artifacts.

## Current Source of Truth

- `README.md` is the English source README.
- `README_es.md`, `README_pt.md`, `README_ja.md`, `README_ko.md`, `README_de.md`, `README_fr.md`, `README_tr.md`, `README_zh-TW.md`, `README_zh-CN.md`, and `README_ru.md` are localized README files.
- `data/use-cases.json` is the public case and source index. It covers every README case number, source, creator, evidence type, and date. New media-backed cases also record their original media and public presentation URLs.
- `docs/update-log.md` records case additions and related maintenance changes.
- There is no active generator that can safely rebuild the finished README files.

## Case Format

The public README uses a custom usecase variant:

- Each case has a stable `<a id="case-x"></a>` anchor.
- Each case heading uses `### Case X:` and links to the original source.
- The first paragraph under the heading is a bold usage takeaway.
- The body keeps readable source-content notes instead of a generic summary label.
- `Type: ... | Date: YYYY-MM-DD` stays near the end of each case.

This intentionally differs from the stricter usecase template:

- No per-case quality badge is shown in public case headings.
- No `How to use it:` label is used.
- No `Tweet excerpt` label is used.
- Code blocks are used only for actual code, prompts, commands, or structured examples.

## Update Checklist

Before adding or changing a case:

- Update the English source README first.
- Keep the same case number, anchor, source link, creator link, type, and date across every localized README.
- Keep the Menu links pointed at the matching `#case-x` anchors.
- Credit every registered creator explicitly in the Acknowledge section.
- Confirm no placeholder translation text remains.
- Confirm every banner image path referenced by a README exists in `images/`.

## Update Intake

Collect public source candidates and deduplicate them against the README source links and `data/use-cases.json`. Review the original creator's post, concrete output, source media, and workflow details before selecting a case. Keep supporting posts attached to the same case rather than counting them as separate projects.

Update English first, then every localized README. Preserve exact prompt text when reproducing a prompt, and keep creator-reported timing and one-shot descriptions attributed to the creator.

Keep raw research collections, review queues, credentials, and temporary verification files outside the public repository. Submit selected content through a pull request.

## Validation Commands

Run these checks before publishing:

```bash
for f in README*.md; do printf '%s ' "$f"; rg -c '^### Case [0-9]+' "$f"; done
for f in README*.md; do printf '%s ' "$f"; rg -c '<a id="case-[0-9]+"></a>' "$f"; done
rg -n 'images/logo\.svg|How to use it:|Tweet excerpt|19 more creators|more creators' README*.md CONTRIBUTING.md
rg -n '<img src="images/' README*.md
```

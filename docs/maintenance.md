# Maintenance Notes

This repository is a curated usecase content repository. The public README files are manually edited source-of-truth documents, not generated build artifacts.

## Current Source of Truth

- `README.md` is the English source README.
- `README_es.md`, `README_pt.md`, `README_ja.md`, `README_ko.md`, `README_de.md`, `README_fr.md`, `README_tr.md`, `README_zh-TW.md`, `README_zh-CN.md`, and `README_ru.md` are localized README files.
- `fable-5-howto-usecase-curated.json` and `fable-5-howto-usecase-curated.md` are the curated dataset files used to audit and update the public cases.
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

## Daily Update Intake Workflow

The repository has a scheduled GitHub Actions workflow at `.github/workflows/daily-update-intake.yml`.

It runs every day at 01:00 UTC / 09:00 Asia-Shanghai and can also be started manually from the Actions tab.

Required repository secret:

- `TWITTERAPI_API_KEY` — twitterapi.io read API key used to search recent X/Twitter posts.

What the workflow does:

- Searches recent public posts for Claude Fable 5 / Fable 5 candidates.
- Deduplicates against links already present in `README*.md` and the curated JSON file.
- Runs lightweight README consistency checks.
- Uploads `daily_update_candidates.json`, `daily_update_issue.md`, and `validation_summary.md` as an artifact.
- Opens or updates one issue named `Daily Fable 5 update intake` with reviewer-ready candidates.

What the workflow intentionally does not do:

- It does not edit README files.
- It does not add cases automatically.
- It does not sync localized READMEs.

This follows the curation boundary used by the local prompt intake skills: collect and deduplicate first, then require human approval before repository content changes.

## Validation Commands

Run these checks before publishing:

```bash
for f in README*.md; do printf '%s ' "$f"; rg -c '^### Case [0-9]+' "$f"; done
for f in README*.md; do printf '%s ' "$f"; rg -c '<a id="case-[0-9]+"></a>' "$f"; done
rg -n 'images/logo\.svg|How to use it:|Tweet excerpt|19 more creators|more creators' README*.md CONTRIBUTING.md
rg -n '<img src="images/' README*.md
```

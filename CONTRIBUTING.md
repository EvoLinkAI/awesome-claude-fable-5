# Contributing

This repository curates high-signal Claude Fable 5 use cases from public sources.

For the current custom usecase format and maintainer validation commands, see [docs/maintenance.md](docs/maintenance.md).

Pull requests should use the repository PR template: [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).

## Case Requirements

New public README cases should match the current case format:

- `### Case X: [Source-grounded title](original-source-link)`
- A bold one-sentence usage takeaway directly under the heading.
- Readable source-content notes that preserve what the creator actually showed or said.
- Creator attribution with handle and profile link.
- `Type: ... | Date: YYYY-MM-DD`
- Stable `<a id="case-x"></a>` anchors for menu links.

Do not add the label `How to use it:`. The usage sentence should stand on its own in bold text.

## Source Evidence

Public cases should be traceable to original sources. Prefer concrete evidence such as prompts, full workflows, benchmark methods, demos, integration steps, cost data, or clearly stated limits.

Quality tiers may be kept in the internal dataset, but the public high-tier README does not show per-case quality badges.

## Attribution

Credit every creator explicitly. Do not replace named creators with phrases such as "more creators" or "additional users".

When source text is included, keep it useful and readable, and always link to the original post or page. Use normal Markdown paragraphs for source-content notes. Use code blocks only for actual code, commands, prompts, or structured examples.

If a creator asks for a correction or removal, update the case promptly.

## Localization

When a case is added or materially changed, update every localized README:

- `README.md`
- `README_es.md`
- `README_pt.md`
- `README_ja.md`
- `README_ko.md`
- `README_de.md`
- `README_fr.md`
- `README_tr.md`
- `README_zh-TW.md`
- `README_zh-CN.md`
- `README_ru.md`

Each localized README should keep the same 60-case structure, anchors, menu links, source links, creator links, and case numbering.

## Maintainer Checklist

- Confirm all case anchors and menu links resolve.
- Confirm every `### Case X` heading has a source link.
- Confirm every registered creator is named in the Acknowledge section.
- Confirm no `How to use it:`, `Tweet excerpt`, or placeholder translation text remains.
- Confirm banner image paths exist for each localized README.
- Confirm the internal dataset and public README stay in sync.

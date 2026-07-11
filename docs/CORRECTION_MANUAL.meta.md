# CORRECTION_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/CORRECTION_MANUAL.md](https://github.com/sanskrit-lexicon/BHS/blob/main/docs/CORRECTION_MANUAL.md)
— purpose, provenance, improvement backlog and revision history of the manual
itself (not of the pipelines it documents).

## Purpose

Give a new operator/contributor a runnable understanding of BHS's correction
pipelines — the commit-pinned issue-campaign pattern (issue1's external-
revision ingest with its 8 custom DTD elements, issue3's unmarked-language
fixes, issue4's tooltip reconciliation), the English-error triage with its
multilingual false-positive machinery, headword normalization, and the
re-runnable meta2 maintenance loop — inside the org's csl-orig batched-PR
delivery rule.

## Audience

- **Operators** opening a new correction campaign or re-running the meta2
  refresh (cheat-sheet, walkthroughs 1/4, symptom table);
- **Reviewers** working the open 180-case
  [bhs_error_todo.txt](https://github.com/sanskrit-lexicon/BHS/blob/main/eng_error_lang/bhs_error_todo.txt)
  queue (walkthrough 2);
- **Maintainers** touching the custom multilingual markup or tooltips
  (special-shape section, appendix invariants).

## Provenance

- Authored 11-07-2026 by Fable 5 (`claude-fable-5`) executing handoff
  [H519-Fable_BHS_correction_pipeline_manual_10.07.26.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/H519-Fable_BHS_correction_pipeline_manual_10.07.26.md)
  — the **last row of the H501–H531 manual-coverage census batch**.
- Modelled on the gold-standard operator manual
  [RussianRamayana Litpam-Indexator MANUAL.md](https://github.com/gasyoun/RussianRamayana/blob/main/Litpam-Indexator/docs/indesign-pipeline/MANUAL.md).
- Source material read first-hand (no subagents — compact repo): README,
  CLAUDE.md, DATA_DICTIONARY, the eng_error_lang/meta/headwordmod readmes,
  issue1/3/4 readmes + `redo.sh`/`hw1.sh`, prefaces README. Commands quoted
  verbatim; counts (4,075 → 3,895 OK + 180 TODO; 1,176 list-marked; 12→452
  change generations; 75 extended-ASCII codes) are from the executed runs'
  notes, with the readme's internal 3,793-vs-3,895 discrepancy flagged
  rather than silently resolved.
- Transcription-verified: paths/scripts confirmed on disk 11-07-2026; no
  pipeline re-executed (all mutate the sibling csl-orig tree or are
  campaign-pinned).

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Work the open 180-case `bhs_error_todo.txt` queue (or re-assign it and record the owner) — the repo's oldest open loose end | open |
| 2 | Live-verify the meta2 loop (`check_ea1.py` + `check_tags.py` against current csl-orig) and record fresh census numbers — the only cheaply re-runnable pipeline here | open |
| 3 | Rewrite CLAUDE.md's self-referential Architecture table from this manual's map, and link the manual | open |
| 4 | Fix `eng_error_lang/readme.txt`'s typo (`.txxt`) and reconcile its 3,793-vs-3,895 OK-count discrepancy against the committed file | open |
| 5 | Register the 8 custom DTD elements in a durable reference (DATA_DICTIONARY.md row or csl-pywork note) — today they're only discoverable in issue1's readme | open |
| 6 | Replace `hw1.sh`'s `Cologne_localcopy` dependency with a documented fetch (or mark the step historical) | open |

## Known limitations

- **Transcription-verified, not re-executed** (see Provenance); backlog #2
  names the cheap upgrade.
- The prefaces workspace is pointed to, not re-documented — its own
  [README](https://github.com/sanskrit-lexicon/BHS/blob/main/prefaces/README.md)
  is complete.
- issue3's per-check command detail is summarized (its readme is the log of
  an iterative wordlist-building session; the change files are the durable
  output).

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/BHS/blob/main/README.md) — repo overview, timeline, prefaces
- [CLAUDE.md](https://github.com/sanskrit-lexicon/BHS/blob/main/CLAUDE.md) — code contract with the annotated entry example
- [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/BHS/blob/main/DATA_DICTIONARY.md) — tag reference
- [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — canonical delivery procedure
- Sibling census-batch manuals: [AP](https://github.com/sanskrit-lexicon/AP/blob/main/docs/PIPELINE_MANUAL.md) · [AP90](https://github.com/sanskrit-lexicon/AP90/blob/master/docs/PIPELINE_MANUAL.md) · [ApteES](https://github.com/sanskrit-lexicon/ApteES/blob/main/docs/TOOLING_MANUAL.md) · [PWK](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md) · [AMAR](https://github.com/sanskrit-lexicon/AMAR/blob/main/docs/CONVERSION_MANUAL.md)

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial manual + this metadoc authored (H519, closing the H501–H531 batch); all dirs read first-hand; 6 traps recorded | Fable 5 (`claude-fable-5`) |

_Dr. Mārcis Gasūns_

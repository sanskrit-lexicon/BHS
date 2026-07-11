# CORRECTION_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/CORRECTION_MANUAL.md](https://github.com/sanskrit-lexicon/BHS/blob/main/docs/CORRECTION_MANUAL.md).

## Purpose

The runbook over BHS's working dirs: the correction pipeline applied to
Edgerton, and the three repo-owned data workflows finally described
(spellcheck error-mining with FR/DE language classification; headword
normalization; the bhs-meta2 display-metadata loop), plus the per-issue
pattern and prefaces.

## Audience

- An operator preparing a BHS correction for the monthly batch.
- A contributor picking up the open threads (#4 tooltips, #5 meta2,
  #2 semantic line breaks).
- Anyone rerunning the error-mining pass after a big correction batch.

## Provenance

Authored 11-07-2026 by Fable 5 (`claude-fable-5`) under handoff
[H519-Fable_BHS_correction_pipeline_manual_10.07.26](https://github.com/gasyoun/Uprava/blob/main/handoffs/H519-Fable_BHS_correction_pipeline_manual_10.07.26.md)
(the H501–H531 per-repo manuals programme, Litpam-Indexator MANUAL.md gold
standard). Content read from the meta/issue readmes, the workflow scripts
(`hw1.py`, `bhs_german.py`, `check_*.py`, `adjust_tooltip.py` context),
README/CLAUDE.md/DATA_DICTIONARY, and the canonical correction-workflow doc
— none invented. Closes the core of
[issue #7](https://github.com/sanskrit-lexicon/BHS/issues/7) (docs-pass).

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Replace the circular "working files" labels in README/CLAUDE.md Contents tables with the §3 one-liners | open |
| 2 | Finish the tooltip revision ([issue #4](https://github.com/sanskrit-lexicon/BHS/issues/4)) — the live workspace | open (owned by issue) |
| 3 | Run the meta2 loop ([issue #5](https://github.com/sanskrit-lexicon/BHS/issues/5)) after the next correction batch | open (owned by issue) |
| 4 | Annotate the copy-paste count residue in `meta/readme.txt` | open |
| 5 | A rerun note for §3.1 (pyspellchecker version pin — lexicon drift changes the miss set between runs) | open |

## Known limitations

- The scholarly adjudication of flagged words (typo vs Edgerton's usage vs
  quotation) is judgment outside this manual; §3.1 documents the mechanics
  and the review files.
- `adjust_tooltip.py` internals are not decoded — issue4's readme is the
  working log of record.
- The build side is the canonical workflow doc's territory.

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/BHS/blob/main/README.md) — repo overview (dated header added in this PR)
- [CLAUDE.md](https://github.com/sanskrit-lexicon/BHS/blob/main/CLAUDE.md) + [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/BHS/blob/main/DATA_DICTIONARY.md) — format references
- Working logs: [meta/readme.txt](https://github.com/sanskrit-lexicon/BHS/blob/main/meta/readme.txt) · [issues/issue4/readme.txt](https://github.com/sanskrit-lexicon/BHS/blob/main/issues/issue4/readme.txt)
- [csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — the canonical 8-stage reference
- Sibling manuals: [csl-orig CORRECTION_MANUAL](https://github.com/sanskrit-lexicon/csl-orig/blob/main/docs/CORRECTION_MANUAL.md) (H515, delivery side) · [BOP CORRECTION_MANUAL](https://github.com/sanskrit-lexicon/BOP/blob/main/docs/CORRECTION_MANUAL.md) (H516, same programme)

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial version (H519) | Fable 5 (`claude-fable-5`) |

---

_Dr. Mārcis Gasūns_

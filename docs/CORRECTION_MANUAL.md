# BHS Correction Manual

_Created: 11-07-2026 · Last updated: 11-07-2026_

The operator manual for correction and enrichment work on Edgerton's
*Buddhist Hybrid Sanskrit Dictionary* (1953, BHS→English, 17,777 entries):
the correction pipeline self-contained, plus the three data workflows this
repo owns — English-spellcheck error triage with French/German language
classification (`eng_error_lang/`), headword normalization
(`headwordmod/`), and the `bhs-meta2.txt` display-metadata upkeep (`meta/`)
— and the per-issue pattern and completed prefaces OCR.

Companion metadoc: [docs/CORRECTION_MANUAL.meta.md](https://github.com/sanskrit-lexicon/BHS/blob/main/docs/CORRECTION_MANUAL.meta.md).

---

## 1. Cheat-sheet — one correction, end to end

```bash
# layout: BHS + csl-orig + csl-pywork as siblings ($BASE/cologne convention)

# 1. snapshot the canonical text (pin the commit in the issue readme)
git -C $BASE/cologne/csl-orig show <hash>:v02/bhs/bhs.txt > temp_bhs_0.txt

# 2. change file (paired lines, ';' comments; new/ins/del; UTF-8, NO BOM)
#    NNN old <exact current line>
#    NNN new <replacement line>

# 3. apply
python updateByLine.py temp_bhs_0.txt change_bhs_N.txt temp_bhs_1.txt

# 4. rebuild + validate (from csl-pywork/v02/)
sh generate_dict.sh bhs ../../bhs
sh xmlchk_xampp.sh bhs

# 5. DELIVER — org agents: correction queue → the ONE consolidated csl-orig
#    PR ~monthly (/cologne-correction-queue + /cologne-batch-pr); direct
#    csl-orig commits are the upstream-maintainer pattern only.
#    Audit trail: diff_to_changes_dict.py → csl-corrections batch.
```

Full 8-stage discipline + every gotcha (BOM, `<LEND>`, CRLF, line-count
mismatch, line drift, python3/xmllint):
[csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md).

## 2. Data-flow diagram

```
csl-orig/v02/bhs/bhs.txt   (canonical; SLP1 {#…#} + ENGLISH glosses {%…%};
│    Edgerton's apparatus is MULTILINGUAL — French/German scholarship quoted
│    inline, tagged <lang>; refs in 〔…〕 lenticular brackets)
│
├── eng_error_lang/  — SPELLCHECK-DRIVEN ERROR MINING (§3.1)
│     bhs_error.txt        L:headword:suspect-word triples (English spellcheck
│     │                    misses over the gloss text)
│     ├─ triage → bhs_error_ok.txt / bhs_error_todo.txt
│     └─ language classification: bhs_french.py / bhs_german.py
│        (pyspellchecker EN/FR/DE lexicons) → bhs_{french,german}(_edit).txt,
│        bhs_misc_edit / bhs_sanmisc_edit / bhs_ok_san
│        → feeds <lang> markup + typo corrections (issue #3, closed)
│
├── headwordmod/  — HEADWORD NORMALIZATION (§3.2)
│     bhshw0.txt (page,col:hw:L1,L2) → hw1.py (strip parentheticals, commas,
│     hyphens, avagraha, one-off mojibake) → bhshw1.txt (+ _note audit)
│     → diff vs the Cologne XML copy → dhavalmodification.txt
│
├── meta/  — bhs-meta2.txt UPKEEP (§3.3; open issue #5)
│     check_ea1.py (extended-ascii census) + check_tags.py (tag census)
│     → statistics → MANUAL revision of bhs-meta2.txt → copy back to csl-orig
│
├── issues/  — per-issue workspaces: issue1 (Andhrabharati corrections,
│     with compare/litsrc/meta sub-passes) · issue3 (multilingual words) ·
│     issue4 (ls-tag tooltip revision, OPEN — adjust_tooltip.py + Anna's
│     abbreviation list) · markup_fix (org fixer family)
│
├── prefaces/  — front-matter OCR, COMPLETE (15 pages: title block,
│     Edgerton's Preface, the full Bibliography & Abbreviations; EN + RU)
│
▼  csl-pywork build → bhs.xml → Cologne display / csl-app
```

## 3. The three data workflows

### 3.1 English-error mining with language classification (`eng_error_lang/`)

**The idea:** run the English gloss text through a spellchecker; every miss
is either a typo, a Sanskrit form, or — Edgerton's specialty — a **French or
German quotation** that needs `<lang>` markup rather than "fixing".
`bhs_error.txt` holds the raw `L:headword:word` misses; triage splits them
into `_ok` (legitimate) and `_todo`. `bhs_french.py` / `bhs_german.py` load
pyspellchecker's EN + FR/DE word lists and classify the residue — a word
unknown to English but known to German is a German-quotation candidate —
producing the `_edit` review files. The closed
[issue #3](https://github.com/sanskrit-lexicon/BHS/issues/3) ("words in
different languages") is this workflow's delivered round; rerunning it after
a big correction batch re-mines the text. Dependency: `pip install
pyspellchecker` (the one third-party package in the repo).

### 3.2 Headword normalization (`headwordmod/`)

`hw1.py` (ejf 2013, utf-8 2014) normalizes the extracted headword list
`bhshw0.txt` — stripping parenthetical variants, comma tails, hyphens,
avagraha apostrophes, and three documented one-off mojibake bytes — into
`bhshw1.txt` (+ `bhshw1_note.txt` audit). `hw1.sh` then diffs the result
against the Cologne XML build's copy; the divergence list is
`dhavalmodification.txt` (Dhaval's side of the reconciliation). This is a
completed pass kept replayable; rerun only when headword policy changes.

### 3.3 meta2 upkeep (`meta/`)

`bhs-meta2.txt` (in csl-orig, beside the source) is the display-metadata
file — the inventory of extended-ASCII characters and tags the display
layer must know about. The loop
([meta/readme.txt](https://github.com/sanskrit-lexicon/BHS/blob/main/meta/readme.txt)):
copy fresh `bhs.txt` + `bhs-meta2.txt` → `check_ea1.py` (extended-ascii
census) + `check_tags.py` (tag census, with a local-tags split) → revise
`bhs-meta2.txt` **manually** against the statistics → copy back to csl-orig
and rebuild. Open thread:
[issue #5](https://github.com/sanskrit-lexicon/BHS/issues/5) (meta2 update).
Run this loop after any batch that adds characters or tags.

## 4. Per-issue corrections and prefaces

`issues/issueNNN/` follows the standard Cologne pattern — pin the input by
commit hash (issue4's readme records `bf5bfd16` exactly; do the same),
transform incrementally, keep change files + readme, rebuild + validate,
deliver per §1 step 5. The open
[issue #4](https://github.com/sanskrit-lexicon/BHS/issues/4) (ls-tag
tooltip revision, `adjust_tooltip.py` + Anna's curated abbreviation list)
is the live workspace. `prefaces/` is complete — 15 pages (title block,
Preface, the dense two-column Bibliography & Abbreviations) in EN + RU; the
README's OCR notes record the main-thread-only constraint for this
dictionary's scans.

## 5. Environment & prerequisites

- **Python 3**; `pip install pyspellchecker` for the §3.1 classifiers
  (everything else stdlib); `sh` via Git Bash on Windows.
- **Sibling repos:** csl-orig (canonical `bhs.txt` + `bhs-meta2.txt`),
  csl-pywork (build/validation), csl-corrections (audit + queue).
- Historical logs use the maintainer XAMPP layout — substitute your paths.

## 6. Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| Spellcheck flags a "typo" that is French/German | Edgerton quotes FR/DE scholarship inline | §3.1 classification first; the fix is `<lang>` markup, not an English "correction" |
| A flagged word is Anglicized Sanskrit | Edgerton's citation style | `bhs_ok_san` / `_sanmisc` territory — never "correct" it to dictionary English |
| `updateByLine.py` mismatch | Change file built against a different bhs.txt state | Re-pin by commit hash (the issue4 pattern) and rebuild the change file |
| Display shows a raw tag or lost character after a batch | `bhs-meta2.txt` not updated for new tags/characters | Run the §3.3 meta loop; issue #5 is the standing tracker |
| `〔…〕` brackets look like corruption | The lenticular brackets are BHS's reference-locus markup by design | Leave them; they are load-bearing for `<ls>` tooltips |
| Headword diff vs XML copy is non-empty | Expected — that's `dhavalmodification.txt`'s purpose (reconciliation input) | Review, don't force to zero |
| `ModuleNotFoundError: spellchecker` | The one pip dependency | `pip install pyspellchecker` |
| Tempted to commit straight to csl-orig | The no-noise delivery rule | Queue it; ONE batched PR ~monthly (§1 step 5) |
| An old issue's fix seems obvious | May already be adjudicated | csl-corrections CFR/batch-history preflight first |

## 7. Glossary

| Term | Meaning |
|---|---|
| BHS | Buddhist Hybrid Sanskrit — the non-classical Sanskrit of Buddhist texts Edgerton codified |
| `〔…〕` | Lenticular brackets around reference loci (page.line of the quoted text editions) |
| `<lang>` | Markup for non-English apparatus words (Skt., Pali, French, German quotations) |
| meta2 (`bhs-meta2.txt`) | The per-dictionary display-metadata file (extended-ascii + tag inventory) living in csl-orig |
| error triage | The `bhs_error → _ok/_todo → language classification` review chain of §3.1 |
| avagraha | The `'` elision mark — stripped in headword normalization |
| `bhshw0/1.txt` | Raw vs normalized headword lists (page,col:hw:L-range format) |
| `dhavalmodification.txt` | The headword divergence list vs the Cologne XML copy — reconciliation input |
| change file | Line-addressed `NNN old`/`NNN new` (+ `ins`/`del`) edit record |
| batched PR | The agent delivery unit into csl-orig: everything queued, one consolidated PR ~monthly |

## 8. Maintainer appendix

- **Live vs finished:** open = tooltip revision (#4), meta2 update (#5),
  semantic line breaks (#2), the docs-pass (#7 — this manual is its core
  deliverable). Finished = AB corrections (#1), multilingual words (#3),
  markup oddities (#6), prefaces, the headwordmod pass.
- **Observed quirks** (11-07-2026, while writing this manual): (1) the
  README and CLAUDE.md "Contents" tables describe the working dirs as
  "`eng_error_lang/` working files" — circular labels; this manual's §3 is
  the missing description; (2) `hw1.py` hardcodes three one-off mojibake
  fixes (`s\xa4`, `\x85yenaiva`…) — historical bytes, don't generalize from
  them; (3) the README lacked the org dated header until this PR (added,
  with the git creation date 16-05-2026); (4) `meta/readme.txt` line 24
  echoes a count from a *different* file (`temp_bhs_ab_1.txt`) — copy-paste
  residue in the log.
- **Cross-repo edges:** csl-orig (canonical text + meta2), csl-pywork
  (build), csl-corrections (audit + queue), the markup_fix family shared
  with BOP/PWG/PWK/LRV.
- **Issue taxonomy:** dictionary-repo taxonomy — see
  [CLAUDE.md](https://github.com/sanskrit-lexicon/BHS/blob/main/CLAUDE.md)
  and [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/BHS/blob/main/DATA_DICTIONARY.md)
  for the tag reference.

---

_Dr. Mārcis Gasūns_

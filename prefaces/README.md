# BHS front matter (prefaces)

Faithful OCR + translation of the **front matter** of **Franklin Edgerton's *Buddhist Hybrid Sanskrit Grammar and Dictionary*, Volume II: Dictionary** (originally Yale University Press, 1953; Motilal Banarsidass reprint, Delhi). Two physical volumes (I = Grammar `bhsg`, II = Dictionary `bhsd`); the Cologne `bhspref` set collects front matter from both.

Source scans (Cologne Digital Sanskrit Dictionaries):
<https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/bhspref.html>

**Source language: English** — base per-page `.md` is the English edition (no separate `.en.md`); a Russian translation `.ru.md` accompanies every page.

> **Status: in progress.** Done: the Dictionary-volume title block (01 Title, 02 Contents, 12 full Title, 13 Copyright, 14 Series half-title) and the Grammar-volume **Preface** (03–05) and the start of the **Bibliography and Abbreviations** (06 intro, 07–08 the text-sigla and the beginning of the general abbreviation list). **Pending:** the rest of the Bibliography & Abbreviations (`bhspref09–11`, scans `bhsg_020–022` — dense multi-column reference lists) and the final Dictionary-volume page (`bhspref15`, scan `bhsd_632`).

## File conventions

| Suffix | What it is |
|---|---|
| `bhsprefNN.md` | Faithful transcription (English source) |
| `bhsprefNN.ru.md` | Russian translation |
| `scans/*.png` | Source scan images |
| `build_combined.py` | Rebuilds the consolidated editions (`DICT=bhs python build_combined.py`) |

## Consolidated editions

| Edition | File |
|---|---|
| English (so far) | [bhspref_all.en.md](bhspref_all.en.md) |
| Russian (so far) | [bhspref_all.ru.md](bhspref_all.ru.md) |

## Contents

| # | Section | Vol. | Source | RU | Status |
|---|---|---|---|---|---|
| 01 | Title | 2 | [bhspref01.md](bhspref01.md) | [ru](bhspref01.ru.md) | ✓ |
| 02 | Contents | 2 | [bhspref02.md](bhspref02.md) | [ru](bhspref02.ru.md) | ✓ |
| 03 | Preface, 1 | 1 | [bhspref03.md](bhspref03.md) | [ru](bhspref03.ru.md) | ✓ |
| 04 | Preface, 2 | 1 | [bhspref04.md](bhspref04.md) | [ru](bhspref04.ru.md) | ✓ |
| 05 | Preface, 3 | 1 | [bhspref05.md](bhspref05.md) | [ru](bhspref05.ru.md) | ✓ |
| 06 | Bibliography & Abbreviations, 1 | 1 | [bhspref06.md](bhspref06.md) | [ru](bhspref06.ru.md) | ✓ |
| 07 | Bibliography & Abbreviations, 2 | 1 | [bhspref07.md](bhspref07.md) | [ru](bhspref07.ru.md) | ✓ |
| 08 | Bibliography & Abbreviations, 3 | 1 | [bhspref08.md](bhspref08.md) | [ru](bhspref08.ru.md) | ✓ |
| 09–11 | Bibliography & Abbreviations, 4–6 | 1 | — | — | pending |
| 12 | Title (full) | 2 | [bhspref12.md](bhspref12.md) | [ru](bhspref12.ru.md) | ✓ |
| 13 | Copyright | 2 | [bhspref13.md](bhspref13.md) | [ru](bhspref13.ru.md) | ✓ |
| 14 | Series half-title | 2 | [bhspref14.md](bhspref14.md) | [ru](bhspref14.ru.md) | ✓ |
| 15 | (Dictionary vol.) | 2 | — | — | pending |

## Notes

- Edgerton's Preface (pp. xxi–xxiii) explains the scope, the deliberate exclusion of standard-Sanskrit words, and the acknowledgements.
- The Bibliography classifies the BHS texts into three linguistic classes and then lists the text sigla (AbhidhK … Vaj) and general abbreviations (the dense reference lists on pp. xxvi ff.).
- Devanāgarī/IAST and the many bibliographic sigla are kept verbatim.

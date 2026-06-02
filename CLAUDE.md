# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**BHS** is the development and correction repository for **Franklin Edgerton's *Buddhist Hybrid Sanskrit Grammar and Dictionary*, vol. 2 (Dictionary)**, a specialized dictionary of Buddhist Hybrid Sanskrit, within the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) (CDSL).

- **Canonical source text**: [`csl-orig/v02/bhs/bhs.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/bhs/bhs.txt) (17,777 entries) — corrections are applied to that file, not stored here.
- This repository holds **development artifacts**: corrections, markup, comparison, and per-issue working files.
- A specialized lexicon of the non-classical Sanskrit of Buddhist texts; entries carry multilingual notes (French, German).

## Architecture

| Path | Purpose |
|---|---|
| `eng_error_lang/` | `eng_error_lang/` working files |
| `headwordmod/` | `headwordmod/` working files |
| `issues/` | Per-issue working files |
| `meta/` | `meta/` working files |

## Key commands

Corrections follow the CDSL `updateByLine.py` pattern, applied against the csl-orig source:

```sh
python updateByLine.py <input> <changefile> <output>
```

Change-file format (paired lines; `;`-prefixed comments):

```
1234 old <original line>
1234 new <replacement line>
```
Supports `new` (replace), `ins` (insert after), `del` (delete). All files UTF-8 (**no BOM**).

## Data format

BHS entries use standard CDSL Sanskrit-lexicography markup. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for the full tag reference.

| Tag | Role |
|---|---|
| `<L>NNNN<pc>PPP` | Entry begin, with print page-column ref |
| `<k1>`, `<k2>` | Primary / secondary headword (SLP1) |
| `<LEND>` | Entry end |
| `{#…#}` | Sanskrit text (SLP1) |
| `{%…%}` | English gloss / italic display text |
| `¦` | Headword / definition separator |
| `<lex>…</lex>` | Lexical category |
| `<ls>…</ls>` | Literary source citation |

Annotated example — the first entry of `bhs.txt`:

```
<L>1<pc>001,1<k1>a<k2>a-, an-
{@a-, an-@}¦, negative prefix: ({@1@}) prefixed to finite verbs, as rarely in <lang>Skt.</lang> (<ls>Renou</ls> 〔p. 175〕) but rather often in <lang>Pali</lang> (<ls>CPD</ls> <ab>s.v.</ab> 7); here not common: apaśyanti <ls>SP</ls> 〔324.2〕; anatikramāmo <ls>Mv</ls> 〔ii.80.8〕; anicchiyati (?) <ls>Mv</ls> 〔iii.295.18〕; see 〔§ 23.17〕; ({@2@}) in sense described for <lang>Pali</lang> in <ls>CPD</ls> <ab>s.v.</ab> 2, a <ab>cpd.</ab> in a- following the same word without a-, and preceding a form of kṛ: samitim asamitiṃ kṛtvā <ls>Divy</ls> 〔41.10〕, <ab>lit.</ab> {%making the assembly no assembly%}, <ab>i.e.</ab> {%quitting the assembly%}; tasya vacanam avacanaṃ kṛtvā <ls>Divy</ls> 〔41.28〕, {%disregarding his advice%}. See {@an-a-@}.
<LEND>
```

## Dependencies

- Python 3 (correction and comparison scripts).
- No build step in this repo; XML and web display are generated centrally from `csl-orig` via `csl-pywork`.

## GitHub Issue Conventions

This repository uses the Cologne dictionary-repo issue taxonomy. Every issue has exactly one **type**, one **severity**, and one **milestone**:

- **Type** (9): link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **Severity** (3): minor, medium, hard
- **Milestone** (4): Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

See the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md) for label definitions and the type→milestone mapping.
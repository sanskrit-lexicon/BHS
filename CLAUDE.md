# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**BHS** is the corrections and research repository for the Cologne digitization of Edgerton's *Buddhist Hybrid Sanskrit Grammar and Dictionary* (1953). The canonical source lives in `csl-orig/v02/bhs/bhs.txt`.

## Architecture

| Directory | Purpose |
|---|---|
| `issues/` | Per-issue correction workflows (`issueNNN/` pattern) |
| `headwordmod/` | Headword identification and modification research |
| `eng_error_lang/` | English spell-check error lists (words found/flagged in spell-checking) |
| `meta/` | Metadata validation: tag checking (`check_tags.py`), entry-attribute checks (`check_ea1.py`), `bhs-meta2.txt` |

### Issue correction pattern (`issues/issueNNN/`)

Each issue folder follows the standard workflow:
1. Copy current `bhs.txt` to a local `temp_bhs_0.txt` (not tracked by git)
2. Apply corrections incrementally as `temp_bhs_1.txt`, `temp_bhs_2.txt`, etc.
3. Rebuild XML with `generate_dict.sh` and validate with `xmlchk_xampp.sh`
4. Commit the corrected file to `csl-orig`, then sync to Cologne
5. Commit issue documentation back here

### Metadata validation (`meta/`)

```bash
python check_tags.py bhs.txt check_tags.txt
python check_ea1.py bhs.txt check_ea1.txt
```

## Common Commands

### Apply line-level corrections
```bash
python updateByLine.py <input_file> <changein_file> <output_file>
```

### Rebuild and validate XML (from `csl-pywork/v02/`)
```bash
sh generate_dict.sh bhs ../../BHSScan/2020
sh xmlchk_xampp.sh bhs
```

## Dependencies

- **Python 3**
- **bhs.txt** — in `$BASE/cologne/csl-orig/v02/bhs/bhs.txt`

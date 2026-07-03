### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `bhs.txt`.

I ran the same two-job recipe over `csl-orig/v02/bhs/bhs.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `issues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — please review the findings listed below.

## Markup fixer + audit for `bhs.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>X</ab> Y</ab>` | `<ab>X Y</ab>` |
| `<ls> word </ls>` | `<ls>word</ls>` |
| `<ab> word </ab>` | `<ab>word</ab>` |
| `<lang> word </lang>` | `<lang>word</lang>` |

Whitespace trimming applies to all 15 paired tag(s) in `bhs.txt`: `<ls>`, `<ab>`, `<lang>`, `<lex>`, `<tib>`, `<ed>`, `<fr>`, `<ger>`, `<hom>`, `<lat>`, `<ms>`, `<bot>`, `<toch>`, `<gk>`, `<zoo>`. The original file is never modified — output goes to `bhs_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format). **Output is byte-identical to source** (no auto-fixes triggered).

### Closing-tag inventory in current `bhs.txt`

| Tag | Count |
|---|---:|
| `</ls>` | 48 |
| `</419)>` | ? |
| `</ab>` | 46 |
| `</676)>` | ? |
| `</lang>` | 18 |
| `</934)>` | ? |
| `</lex>` | 15 |
| `</286)>` | ? |
| `</tib>` | 3 |
| `</193)>` | ? |
| `</ed>` | 409 |
| `</fr>` | 313 |
| `</ger>` | 182 |
| `</hom>` | 171 |
| `</lat>` | 157 |
| `</ms>` | 58 |
| `</bot>` | 15 |
| `</toch>` | 4 |
| `</gk>` | 2 |
| `</zoo>` | 1 |

### What it found in current `bhs.txt`

- 0 whitespace trims — byte-identical to source.
- 1 `<ab n="?">` placeholder: needs expansion lookup.
- 308 within-line `<ab n="…">` non-standard expansion matches — these are Buddhist proper names (Tathāgata ×43, Bodhisattva ×36, Kāśyapa ×8, etc.). All appear intentional; decide whether to standardise or retain.
- 1,163 within-line adjacent `</ab> <ab>` pairs for verification.
- 70 `{{old → new || …}}` correction records present.
- 15 paired tag types — the richest tag set of all dictionaries processed so far.

### Usage

```
cd issues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/bhs/bhs.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `bhs_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

169 unique non-standard n= values (Buddhist names).

### Severity

`minor`

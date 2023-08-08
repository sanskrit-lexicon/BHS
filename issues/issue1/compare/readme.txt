BHS/issues/issue1/compare/readme.txt


wc -l temp_bhs*
  142612 temp_bhs_0.txt
   71444 temp_bhs_ab_1.txt
So, ab's text has only half as many lines.
  Why is that?

Reason:  cdsl version preserves line-breaks, but AB version does not!
But AB version adds markup, so the number of characters is more in
  AB version than in cdsl version:
wc -c temp_bhs*
 5989200 temp_bhs_0.txt
 7589046 temp_bhs_ab_1.txt

--------------------------------------------------------------------------
7651 matches for "- *$" in buffer: temp_bhs_0.txt
  These are lines where a '-' presumuably indicates a line-break in the
  middle of a word.  These are resolved in AB version
--------------------------------------------------------------------------
17839 matches for "^<L>" in buffer: temp_bhs_ab_1.txt
17839 matches for "^<L>" in buffer: temp_bhs_0.txt

So AB version has same number of entries as cdsl.

--------------------------------------------------------------------------

AB version adds markup
1. <ls>X</ls>  literary source name
   48265 matches in 16294 lines for "<ls>" in buffer: temp_bhs_ab_1.txt
1a. <ls n="T">X</ls>  local literary source
  8 matches in 3 lines for "<ls n" in buffer: temp_bhs_ab_1.txt
2.  〔Y〕 literary source details?
   Usually preceded by <ls>
   39346 matches in 16203 lines for "[>] 〔" in buffer: temp_bhs_ab_1.txt
   14665 matches in 5045 lines for "[^>] 〔" in buffer: temp_bhs_ab_1.txt
3. <ab></ab> common abbreviation -- to be added to bhsab tooltips
   45714 matches in 15268 lines for "<ab>" in buffer: temp_bhs_ab_1.txt
3a. <ab n="T">X</ab>  local common abbreviation
   300 matches in 222 lines for '<ab n="' in buffer: temp_bhs_ab_1.txt
4. AB [Page001-b]
   cdsl [Page001-b+ 61]
5. <lang> tag  abbreviation for the name of a language
18945 matches in 8890 lines for "<lang>" in buffer: temp_bhs_ab_1.txt
6. <hom> tag
7. <lex> tag
8. <tib> tag
--------------------------------------------------------------------------
Comparison of headwords
mkdir compare
---------------
compare_hw

python compare_hw.py ../temp_bhs_0.txt ../temp_bhs_ab_1.txt compare_hw.txt
444 differences written to compare_hw.txt

Note: the differences are in 'k2'.
  For all metalines, the L,pc,k1 fields agree.

---------------
compare_text
 Try removing markup from the body text and comparing
 
python compare_text.py ../temp_bhs_0.txt ../temp_bhs_ab_1.txt compare_text.txt

Except for 2 entries, all the AB entries have exactly 1 line.
These two exceptions are:
<L>18<pc>001,2<k1>akalpika<k2>akalpika        3 lines
<L>24<pc>001,2<k1>akAmakAmin<k2>a-kAmakAmin   2 lines
The extra lines start with a '+' character.
---------------

Statistics re text 'blob' size for entries.

python textsize.py ../temp_bhs_ab_1.txt textsize.txt

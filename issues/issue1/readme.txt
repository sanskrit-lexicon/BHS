07-20-2023
Andhrabharati's improvements to bhs digitization.
Ref: https://github.com/sanskrit-lexicon/BHS/issues/1

Probable outcome: revision to csl-orig/v02/bhs/bhs.txt

------------------------------------------------------
Start with:
1a. temp_bhs_ab_1_orig.txt  copy from BHS-ab(Tib done).zip.  See issue1 above.
   AB's revision
   
1b. temp_bhs_ab_1.txt 
cp temp_bhs_ab_1_orig.txt temp_bhs_ab_1.txt
Apply manual corrections as needed.
change_ab_1.txt

2. BHS.Grammar_Front.pages.txt
   varying formats.  To be used for tooltips for <ab> and <ls> tags.
3. temp_bhs_0.txt
   cp /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt temp_bhs_0.txt
   at commit 4600839932897d9bdc8a982315de2c342334acce
   Local file is dated Dec 16, 2021.
   This is close to the Oct 12, 2021 date of most comments in bhs/issues/1
--------------------------------------------------------------------------
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

--------------------------------------------------------------------------
local dev display
sh redo.sh 1
url to access dev1 displays:
http://localhost/sanskrit-lexicon/bhs/issues/issue1/dev1/web/

# xml validity?
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/bhs.xml dev1/pywork/bhs.dtd
12 records records not parsed by ET
# change_1_ab.txt
# changes made.
python diff_to_changes_dict.py temp_bhs_ab_1_orig.txt temp_bhs_ab_1.txt change_1_ab.txt
12 changes written to change_1_ab.txt

# changes to one.dtd

<!ELEMENT tib (#PCDATA) > <!-- Tibetan text, bhs-->
<!ELEMENT ger (#PCDATA) > <!-- German text, bhs-->
<!ELEMENT fr (#PCDATA | i | ab)* > <!-- French text, bhs-->
<!ELEMENT acr (#PCDATA) > <!-- acronym bhs-->
<!ELEMENT ed (#PCDATA) > <!-- edition bhs-->
<!ELEMENT ms (#PCDATA) > <!-- manuscript bhs-->
<!ELEMENT lat (#PCDATA) > <!-- latin text bhs-->
<!ELEMENT toch (#PCDATA) > <!-- Tocharian text bhs-->

--------------------------------------------------------------------------
litsrc directory 
 <ls> element. Including abbreviations from BHS frontmatter.
 also, <ab>, <lex>, <lang> elements
 see litsrc/readme.txt
Note change_1_ab.txt revised:
python diff_to_changes_dict.py temp_bhs_ab_1_orig.txt temp_bhs_ab_1.txt change_1_ab.txt
452 changes  (mostly 'acr' -> 'ab')

--------------------------------------------------------------------------

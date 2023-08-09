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
compare folder.
 see compare/readme.txt
 Various comparisons between Andhrabharati's revision and cdsl version.
 
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
meta directory
 work to update the bhs-meta2.txt file of csl-orig
 
--------------------------------------------------------------------------
--------------------------------------------------------------------------

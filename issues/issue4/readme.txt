bhs/issue4/readme.txt
ls tag tooltips for bhs dicitionary
begun 12-26-2024 ejf

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue4/

# issue 4 link
 https://github.com/sanskrit-lexicon/BHS/issues/4

# start with temp_bhs_0.txt as copy of
  csl-orig/v02/bhs/bhs.txt at current commit
   bf5bfd1658d336895d824e78e46bbd3c6e6d18f4
cd /c/xampp/htdocs/cologne/csl-orig
git show bf5bfd16:v02/bhs/bhs.txt > /c/xampp/htdocs/sanskrit-lexicon/bhs/issues/issue4/temp_bhs_0.txt

# start with copy of ls tooltips for bhs
 temp_ls_0.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsauth/tooltip.txt temp_ls_0.txt

# two files uploaded by Anna
Ref: https://github.com/sanskrit-lexicon/BHS/issues/4#issuecomment-2532884921

tagcount_ls_anna_10.12.24.txt
 comparable to temp_ls_0.txt

temp_BHS.Comments.10.12.24.docx
  Viewable with Microsoft word,
  or google docs.

cp ../issue3/compare/tagcount_ls.txt tagcount_ls_0.txt

cp tagcount_ls_anna_10.12.24.txt tagcount_ls_anna_0.txt
# Jim will do some editing
--- edit 1
insert following line to tagcount_ls_anna_0.txt as line 901 (AB noticed)
   1	ls	Walde-Pokorny  	?
replace  = U+001E Information Separator Two  with a space. 3 instances
 at lines 94, 386, 388
--- edit 2  line 36  (line 70843 of bhs.txt)
old: Andersen, Reader, Glossary
new: Andersenʼs Reader, Glossary
--- edit 3  line 130,
old: ::
new: ;;


python compare_tagcount_ls.py tagcount_ls_0.txt tagcount_ls_anna_0.txt compare_tagcount_ls_0.txt

BHS.Grammar_Front.pages.txt
  https://github.com/sanskrit-lexicon/BHS/tree/master/issues/issue1

cp ../issue1/BHS.Grammar_Front.pages.txt BHS.Grammar_Front.pages.txt
  Who typed this??

# bhsfm_abbr.txt
Lines from BHS.Grammar_Front.pages.txt of form 'X<TAB>= Y'
  (351)
 initialize countstr=0, lsstr 'ls' (capital), 'ab' (lower)

Changed lines 21, 120, and 344 in  BHS.Grammar_Front.pages.txt
  remove extra 'tab' character.

python extract_bhsfm_abbr.py BHS.Grammar_Front.pages.txt bhsfm_abbr_0.txt
 Extract those lines.
350 records written to bhsfm_abbr_0.txt
nab=123, nls=227

cp bhsfm_abbr_0.txt bhsfm_abbr.txt
# manual edit bhsfm_abbr.txt
See readme_bhsfm_abbr.txt 

-------------------------------------------

cp tagcount_ls_0.txt tagcount_ls_0_edit.txt
cp tagcount_ls_anna_0.txt tagcount_ls_anna_0_edit.txt

----------------------------
changes to tagcount_ls_0_edit.txt
see readme_tagcount_ls_0.txt

----------------------------
changes to tagcount_ls_anna_0_edit.txt
Manual changes to tagcount_ls_anna_0_edit.txt
see readme_tagcount_ls_anna_0.txt

----------------------------
Some typos found in bhs.txt
cp temp_bhs_0.txt temp_bhs_1.txt
Manual changes to temp_bhs_1.txt
See readme_bhs_1.txt

-----------------------------------------
# update  'lsstr' field to 'lsfm' based on bhsfm_abbr.txt
# make this change to tagcount_ls_0.txt
# the 'diff' file contains cases where
  - tagcount abbreviation is among the front matter abbreviations
  - BUT the tagcount tooltip differs from the front matter tooltip.
  
python mark_lsfm.py bhsfm_abbr.txt tagcount_ls_0_edit.txt tagcount_ls_1.txt tagcount_ls_1_diffs.txt
adjust_lsstr changed 126 records
0 of these with different tooltips
973 records written to tagcount_ls_1.txt
0 diffs written to tagcount_ls_1_diffs.txt

python mark_lsfm.py bhsfm_abbr.txt tagcount_ls_anna_0_edit.txt tagcount_ls_anna_1.txt tagcount_ls_anna_1_diffs.txt

adjust_lsstr changed 126 records
0 of these with different tooltips
967 records written to tagcount_ls_anna_1.txt
0 diffs written to tagcount_ls_anna_1_diffs.txt

python adjust_tooltip.py tagcount_ls_anna_1.txt adjust_tooltip_anna.txt tagcount_ls_anna_1a.txt 
4 changes read from adjust_tooltip_anna.txt
17 records with tooltip change
967 records written to tagcount_ls_anna_1a.txt

python compare_tagcount_ls.py tagcount_ls_1.txt tagcount_ls_anna_1a.txt compare_tagcount_ls_1a.txt
973 records written to compare_tagcount_ls_1a.txt


*****************************************************
# rewrite comparison file using version 1
python compare_tagcount_ls.py tagcount_ls_1.txt tagcount_ls_anna_1.txt compare_tagcount_ls_1.txt





-----------------------------------------
Anna's comment file mentions line numbers in bhs.txt.
She is using commit f8cae634ee7cedfbcce1044bfa7c58c7557b05da of csl-orig,
I think.

The next commit coalesced all the lines of entries,
   (7c848d6546389c6c8d7612819dde0cce89601a6d)


-----------------------------------------
TODO ?
1 <ab n="Abhidh-s.">Abh</ab>
-----------------------------------------


-----------------------------------------
install temp_bhs_1.txt into csl-orig

cp temp_bhs_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt
cd /c/xampp/htdocs/cologne/csl-orig
git add .
git commit -m "bhs.
Ref: https://github.com/sanskrit-lexicon/BHS/issues/4 - bhs version 1"
git push

-----
# sync csl-orig at Cologne server
git pull
# regen bhs displays

-----
# sync this repo to Github
cp tagcount_ls_anna_1a.txt tagcount_ls_jim_29.12.24.txt

diff -w tagcount_ls_anna_10.12.24.txt tagcount_ls_jim_29.12.24.txt > diff_10.12.24_29.12.24.txt


git add .
git commit -m "#4  version tagcount_ls_jim_29.12.24.txt"

-----------------------------------------

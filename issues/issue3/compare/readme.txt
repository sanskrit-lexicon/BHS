BHS/issues/issue3/compare/readme.txt


compare abbreviations between cdsl version and Andhrabharati version

--------------------------------------------------------------------------
headwords

-------------------------------------------------------------------------
17839 matches for "^<L>" in buffer: temp_bhs_ab_2.txt
17839 matches for "^<L>" in buffer: temp_bhs_4.txt

So AB version has same number of entries as cdsl.

--------------------------------------------------------------------------

python compare_hw.py ../temp_bhs_4.txt ../temp_bhs_ab_2.txt compare_hw.txt
2 differences in metalines
2 differences written to compare_hw.txt

# add two changes to ../check4_edit.txt and regenerate temp_bhs_4.txt
# rerun compare_hw
python compare_hw.py ../temp_bhs_4.txt ../temp_bhs_ab_2.txt temp_compare_hw.txt
0 differences in metalines

--------------------------------------------------------------------------
# get local copy of bhsab_input.txt (tooltips for '<ab>' and related tags)

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsab/bhsab_input.txt .

revisions:
cp bhsab_input.txt  bhsab_input_new.txt
edit bhsab_input_new.txt.
New entries:

--------------------------------------------------------------------------
We begin an iterative process of resolving the differences.

Begin with copies:
cp ../temp_bhs_4.txt temp_bhs_5.txt
cp ../temp_bhs_ab_2.txt temp_bhs_ab_3.txt

Manual changes are made to temp_bhs_5.txt and temp_bhs_ab_3.txt.

The iterative process:
# 1. run this program (for a particular value of 'tag' in the
'compare' function of compare_abbrevs.py):

python compare_abbrevs.py ../temp_bhs_5.txt ../temp_bhs_ab_3.txt temp.txt
# 2. Resolve the difference by editing bhs_5 or bhs_ab_3.
# 2a. Add (or revise) tooltips in bhsab_input_new.txt
#      or bhsauth_tooltip_new.txt
# go back to step 1.
#  Keep iterating until no differences in the particular tag.
#  Then do the whole process again for the next tag
#  Keep going until resolution of all differences for all tags

After the changes, here are the counts of tags.
ab 46230 tags
fr 313
ger 184
gk 2
lat 20
tib 3193
toch 4
bot 15
zoo 1
<ab n="X">Y</ab>  308
<lang n="X">Y</lang> 0
lang 18933
ed 409
hom 171
lex 15286
ms 58
ls 48424


-------------------------------
suggest bhs_ab_3.txt changes:

See changes_bhs_ab_3.txt for itemization of the changes made to bhs_ab_3.txt:


********************************************************************
ls
--------------------------------------------------------------------------
# get local copy of bhsab_input.txt (tooltips for '<ab>' and related tags)

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsauth/tooltip.txt bhsauth_tooltip.txt

revisions:
cp bhsauth_tooltip.txt  bhsauth_tooltip_new.txt
edit bhsauth_tooltip_new.txt.
----
# new ls-tooltips




# Removed from tooltips:
Yogācāras in ‘le commentaire de ĽAbhidharma’	?

-----------------------------------------------------------------
Tags with tooltips in bhsab_input.txt
ab, lang, ed, lex, ms,

python tagcount.py ab ../temp_bhs_5.txt bhsab_input_new.txt tagcount_ab.txt
424 Tooltips from bhsab_input_new.txt
unused:  d.h.   <id>d.h.</id> <disp>Das heißt (German for "that is"</disp>


python tagcount.py ls ../temp_bhs_5.txt bhsauth_tooltip_new.txt tagcount_ls.txt
17839 entries found
976 Tooltips from bhsauth_tooltip_new.txt
0 tips are unused

-----------------------------------------------------------------
-----------------------------------------------------------------
# count remaining differences (after resolution of tag differences)
python textdiff_count.py ../temp_bhs_5.txt ../temp_bhs_ab_3.txt
304 entries (out of 17839) are different.

cp ../temp_bhs_5.txt ../temp_bhs_6.txt


cp ../temp_bhs_ab_3.txt ../temp_bhs_ab_4.txt
# look for first instance where corresponding lines of bhs_6 and ab_4 differ.
# Manual resolve the difference by changing temp_bhs_6.
python compare_texts.py ../temp_bhs_6.txt ../temp_bhs_ab_4.txt temp.txt
#These changes itemized in compare_texts_notes.txt.
# iterate until no differences remain.


NO changes were made to temp_bhs_ab_4, which remains the same
as temp_bhs_ab_3.
We can remove the duplicate
rm ../temp_bhs_ab_4.txt

# confirm there are now no differences:
diff ../temp_bhs_6.txt ../temp_bhs_ab_3.txt
# no output -- the files are identical.
-----------------------------------------------------------------

-----------------------------------------------------------------
# make and check local installation

cp bhsab_input_new.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsab/bhsab_input.txt

cp bhsauth_tooltip_new.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsauth/tooltip.txt

cp ../temp_bhs_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt

cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh bhs  ../../bhs
sh xmlchk_xampp.sh bhs
# ok!

cd /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue3/compare/
-----------------------------------------------------------------

--- sync this repository to github
cd /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue3/compare/
git add .
git commit -m "'compare' directory markup changes. #3"
git push

manually upload ../ temp_bhs_6.txt as latest version of bhs.txt

****************************************************************
Further (minor) revisions based on
  https://github.com/sanskrit-lexicon/BHS/issues/3#issuecomment-1685775888

cp ../temp_bhs_6.txt ../temp_bhs_7.txt
Manually change temp_bhs_7 and
document in changes_bhs_ab_3a.txt
Note: Also revised bhsauth_tooltip_new.txt

python tagcount.py ls ../temp_bhs_7.txt bhsauth_tooltip_new.txt tagcount_ls.txt
978 tip counts written tagcount_ls.txt

-----------------
# Revise local install

cp bhsauth_tooltip_new.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsauth/tooltip.txt
cp ../temp_bhs_7.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/

sh generate_dict.sh bhs  ../../bhs
sh xmlchk_xampp.sh bhs
## PROBLEM validating!
Element lat was declared #PCDATA but contains non text nodes
Solution: Revise one.dtd
OLD:
<!ELEMENT lat (#PCDATA) > <!-- latin text bhs-->
NEW:
<!ELEMENT lat (#PCDATA | i | ab)* > <!-- latin text, bhs-->

sh xmlchk_xampp.sh bhs
## Now OK!
cd /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue3/compare/
---------------
Cologne install
csl-orig
csl-pywork

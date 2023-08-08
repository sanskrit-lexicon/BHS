litsrc/readme.txt


-----------------------------------------------
general abbreviations (<ab> element).

python prepare_ab.py ../temp_bhs_ab_1.txt extract_ab.txt extract_ab_local.txt

71444 lines from ../temp_bhs_ab_1.txt
219 global ab tags
45714 ab tag instances found
219 lines written to extract_ab.txt
69 local ab tags
300 local ab tag instances found
69 lines written to extract_ab_local.txt


-----------------------------------------------
lex tag abbreviations
 All are general
python prepare_lex.py ../temp_bhs_ab_1.txt extract_lex.txt 

71444 lines from ../temp_bhs_ab_1.txt
108 global lex tags
15277 lex tag instances found
108 lines written to extract_lex.txt

-----------------------------------------------
lang tag abbreviations
 All are general
python prepare_lang.py ../temp_bhs_ab_1.txt extract_lang.txt 

71444 lines from ../temp_bhs_ab_1.txt
18945 lang tag instances found
46 lines written to extract_lang.txt

-----------------------------------------------
front_ab.txt abbreviations that we mark as 'ab','lex','lang'.

These are drawn from ../BHS.Grammar_Front.pages.txt
format is
SRC<TAB>ABBREV<TAB>= TOOLTIP
where SRC is a source code for the tooltip
SRC meaning
FR0 directly from the front matter

; ***************************************************

python match_ab.py front_ab.txt match_ab.txt temp_front_work.txt extract_ab.txt extract_lex.txt extract_lang.txt 

There are 5 abbreviations A which appear both as <lex>A</lex> and <ab>A</ab>
 Ref: https://github.com/sanskrit-lexicon/BHS/issues/1#issuecomment-1656656007
 Changes in temp_bhs_ab_1.txt:
   L=6654: <ab>accs.</ab> -> <lex>accs.</lex>
   L=14471: <ab>conj.</ab> -> <lex>conj.</lex>
   L=8556: <ab>derivs.</ab> -> <lex>derivs.</lex>
   L=16569 : <ab>nom.</ab> -> <lex>nom.</lex>
 Regenerate ../change_ab_1.txt (see ../readme.txt)
 
 Regenerate:
python prepare_lex.py ../temp_bhs_ab_1.txt extract_lex.txt 
 108 global lex tags
 15277 lex tag instances found
python prepare_ab.py ../temp_bhs_ab_1.txt extract_ab.txt extract_ab_local.txt
 215 global ab tags
 45709 ab tag instances found

python match_ab.py front_ab.txt match_ab.txt temp_front_work.txt extract_ab.txt extract_lex.txt extract_lang.txt 

Two remain:
check_dups found dup abbrev: "acc."
  OLD  ab acc.::932
  NEW  lex acc.::615
   tooltip: according; accusative
check_dups found dup abbrev: "n."
  OLD  ab n.::6542
  NEW  lex n.::45
  tooltip: name; nominative

[But, the n. in <ab>n. act.</ab>, <ab>n. ag.</ab>, <ab>n. pl.</ab>, <ab>n. pr.</ab>, <ab>n. sg.</ab> is to be expanded as nominative.]

-----------------------------------
Possible mis-labeling
1 <lang>JM</lang> -> <ls>JM</ls>  Jaina Māhārāṣṭrī.
41 <lang>JM.</lang> -> <ls>JM.</ls>  Jaina Māhārāṣṭrī.
3  <lang>Mg.</lang> -> <ab>Mg.</ab> meaning
2 <ab>Bodhicaryāv.</ab> -> <ls>Bodhicaryāv.</ls>
1 <ab>Dh</ab>   ->  Dh   (no markup)
2 <ab>P.K.</ab> -> <ab n="Pūraṇa Kāśyapa">P.K.</ab>
antareṇa , instr. of n. used as adv. and prep.
    neither 'name' nor 'nominative' tooltip makes sense ?
    
-----------------------------------------------

python match_ab_final.py front_ab.txt match_ab_final.txt front_ab_unused.txt extract_ab.txt extract_lex.txt extract_lang.txt 

python make_ab_tooltip.py match_ab_final.txt ab_tooltip.txt
367 lines written to ab_tooltip.txt

-----------------------------------------------
installation of abbreviation tooltips (bhsab)
--- bhsab_input.txt
cp ab_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsab/bhsab_input.txt

**********************************************
Revisions to csl-pywork, csl-websanlexicon related to ab
--- csl-pywork/v02/inventory.txt
add bhs to the abbreviations section

--- csl-pywork/v02/makotemplates/pywork/redo_postxml.sh
add 'bhs' to the list for abbreviations.

--- csl-websanlexicon/v02/makotemplates/webtc/basicadjust.php
convert <lex> and <lang> tags to <ab> tags.

; ***************************************************
  TODO: adapt to BHS : <ls> tag.
; ***************************************************
Work with <ls> tag.
This appears primarily in the form <ls>X</ls>
 A few are 'local' i.e. of form <ls n="A">X</ls> 

extract_ls.txt extract_ls_local.txt show these instances.

python prepare_ls.py ../temp_bhs_ab_1.txt extract_ls.txt extract_ls_local.txt


Regarding local abbreviations (only 8)
-  <ls n="Foucaux">F.</ls> appears 2 times.
-  <ls n="ŚsP">²</ls> appears 6 times

Change ../temp_bhs_ab_1.txt :
-----------------------------------------------
changes to temp_bhs_ab_1 related to <ls> tags
---
 <ls>F.</ls> does Not occur  Change above to global <ls>F.</ls>
 change above to global <ls>ŚsP²</ls>

---
OLD: <ab>ms.</ab> <ls>127. V 1</ls>
NEW: <ab>ms.</ab> 〔127. V 1〕
---
AbidhK. LaV-P. -> AbhidhK. LaV-P.
---
BSOS 1
-----------------------------------------------
Redo extracts:
python prepare_ls.py ../temp_bhs_ab_1.txt extract_ls.txt extract_ls_local.txt
71444 lines from ../temp_bhs_ab_1.txt
910 global ls tags
48270 ls tag instances found
910 lines written to extract_ls.txt
0 local ls tags
0 local ls tag instances found
0 lines written to extract_ls_local.txt

There is no overlap in ls abbreviations between the global and local.
  Thus, no need for the 'local' forms.

-----------------------------------------------
front_ls.txt abbreviations that we mark as 'ls'.
  252 ls abbreviations in front_ls.txxt.
These are drawn from ../BHS.Grammar_Front.pages.txt
format is
SRC<TAB>ABBREV<TAB>= TOOLTIP
where SRC is a source code for the tooltip
SRC meaning
FR0 directly from the front matter
FR1 inferred.

-----------------------------------------------
python match_ls.py front_ls.txt match_ls.txt temp_front_work.txt extract_ls.txt
 initially find matches in front_ls for 132 ls abbreviations in extract_ls.
 779 UNMATCHED.
48270 total extract count
910  # lsrecs

match: finds tooltips for 163 records (43563 instances)
match: finds tooltips for 252 records (43839 instances)
match: finds tooltips for 312 records (44505 instances)
match: finds tooltips for 378 records (46947 instances)
match: finds tooltips for 459 records (47115 instances)
There are now (- 48270 47115) = 1155 instances of <ls>X</ls> with X not matched.
  And these occur in 451 abbreviations X.

Given all of these 451 a tooltip of '?' in ls_front.txt
Now the matching matches everything:
python match_ls.py front_ls.txt match_ls.txt temp_front_work.txt extract_ls.txt

python match_ls.py front_ls.txt match_ls.txt temp_front_work.txt extract_ls.txt

In front_ls.txt, a tool tip of form {X} is to be resolved as the tooltip of
  abbreviation X
-----------------------------------------------
###############################################
version 1 not used
# python match_ls_final.py front_ls.txt match_ls_final.txt front_ls_unused.txt extract_ls.txt

910 pre-tooltip records written to match_ls_final.txt
init_front: 256 tooltip pointers resolved
116 unused front-matter abbreviations written to front_ls_unused.txt

python make_ls_tooltip.py match_ls_final.txt ls_tooltip.txt
910 lines written to ls_tooltip.txt
###############################################

python match_ls_final.py front_ls.txt extract_ls.txt match_ls_final.txt

1026 abbreviations read from match_ls_final.txt
 258 tooltip pointers resolved
910 tooltips written to ls_tooltip.txt
116 front matter with no instances (not written to ls_tooltip.txt
47115 instances with an assigned tip
451 abbreviations with ? as tip
1155 instances with ? as tip


-----------------------------------------------

# upload to csl-pywork
cp ls_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsauth/tooltip.txt

cd ../
sh redo.sh 1
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/bhs.xml dev1/pywork/bhs.dtd
# ok

***********************************************
Changes to csl-pywork, csl-websanlexicon
***********************************************
-----------------------------------------------
csl-pywork/v02 edits:
0. modify make_xml.py
%if dictlo == 'bhs':
 # 07-27-2023
 x = x.replace('〔','')
 x = x.replace('〕','')
%endif

1. modify inventory.txt
ben ap90 sch gra bhs:pywork/${dictlo}auth/redo.sh:CD
ben ap90 sch gra bhs:pywork/${dictlo}auth/readme.org:CD
ben ap90 sch gra bhs:pywork/${dictlo}auth/tooltip.txt:CD
ben ap90 sch gra bhs:pywork/${dictlo}auth/tooltips.sql:CD

2.modify makotemplates/pywork/redo_postxml.sh

# literary source.
%if dictlo in ['mw','pw','pwg','ap90','ben','pwkvn','sch','gra','bhs']:
 cd ${dictlo}auth
 sh redo.sh
 cd ../ # back to pywork
%endif

3. initialize distinctfiles/bhs/pywork/bhsauth  directory
3a. Copy distinctfiles/ben/pywork/benauth to
         distinctfiles/bhs/pywork/bhsauth
3b. edit files in bhsauth - change ben to bhs
   readme.org, redo.sh, tooltips.sql
3c. tooltips.txt has format
 abbrev<TAB>tip
-----------------------------------------------
csl-websanlexicon/v02 edits:
basicadjust.php
in function line_adjust, add 'bhs' to the list of "MW-type" author files.
1.
}else if (in_array($this->getParms->dict,
           array('mw','ap90','ben','sch','gra','bhs'))){
2.
  }else if (in_array($dict,array('mw','ap90','ben','sch','gra','bhs'))){
   $this->dal_auth = new Dal($dict,"authtooltips");
3. in function ls_callback_mw,
  } else if (in_array($this->dict,array('ap90','ben','sch','gra','bhs'))) {
   in function ls_callback_mw:
  }else if ($this->dict == 'bhs') {
   $href = $this->ls_callback_mw_href($code,$n,$data);
    
-----------------------------------------------
-----------------------------------------------
# remake version 1
cd ../ # to issue1 folder
sh redo.sh 1
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/bhs.xml dev1/pywork/bhs.dtd
************************************************
08-07-2023 revisions
-----
Manual revisions to temp_bhs_ab_1.txt,
  match_ab_final.txt, and match_ls_final.txt
related to https://github.com/sanskrit-lexicon/BHS/issues/1#issuecomment-1666562490
Regnerate ../change_1_ab.txt
cd ../
python diff_to_changes_dict.py temp_bhs_ab_1_orig.txt temp_bhs_ab_1.txt change_1_ab.txt
-----------------------------------------------
<acr> (acronym) tag.
Ref: https://github.com/sanskrit-lexicon/BHS/issues/1#issuecomment-1666569893

---
cp temp_bhs_ab_1.txt temp_bhs_ab_1_acr.txt
---
In temp_bhs_ab_1.txt,
change <acr> -> <ab>,  </acr> -> </ab>  (466 occurrences)
---
Remove 'acr' element from one.dtd (in csl-pywork)
---
Add entries to match_ab_final.txt
------------------------------------------------
bhsheader correction:
csl-orig/v02/bhs/bhsheader.xml

Ref: https://github.com/sanskrit-lexicon/BHS/issues/1#issue-1023800161
Serling -> Sterling
------------------------------------------------
regen tooltips
python make_ab_tooltip.py match_ab_final.txt ab_tooltip.txt
375 lines written to ab_tooltip.txt
install:
cp ab_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsab/bhsab_input.txt

python make_ls_tooltip.py match_ls_final.txt ls_tooltip.txt
1026 abbreviations read from match_ls_final.txt
 260 tooltip pointers resolved
910 tooltips written to ls_tooltip.txt
116 front matter with no instances (not written to ls_tooltip.txt
47154 instances with an assigned tip
449 abbreviations with ? as tip
1116 instances with ? as tip

cp ls_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsauth/tooltip.txt
---
Note: changed <lang n="Māgadhi">Mg.</lang> to <ab n="Māgadhi">Mg.</ab>
  as the <lang n="X>Y</lang> has a different sense.
---
change make_xml.py so that text within 〔〕is displayed with class ls (smaller,
gray)
 x = x.replace('〔',"<span class='ls'>")
 x = x.replace('〕','</span>')

---
Regenerate dev1 displays
cd ../
sh redo.sh 1
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/bhs.xml dev1/pywork/bhs.dtd
--------------------------------------
08-07-2023 revisions (END)
************************************************

08-08-2023 revisions (BEGIN)
-----
correct error in match_ab_final.txt
  under Skt.
python make_ab_tooltip.py match_ab_final.txt ab_tooltip.txt

cp ab_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsab/bhsab_input.txt

-----
basicdisplay
Andhrabharati suggestion:
 " tib-, fr- and ger- strings differently from the rest (eng-) of the text
  [may be in a different colour/background, say yellow]; "

sthndl function
For fr- and ger- and tib-
<span style='color: brown;' title='French language'>...</span>
etc.
NOTE: tried beige and yellow, but text hard to read. brown may be ok,
 noticeable but not obtrusive.
 
endhndl function
  </span>
-----
font.css
i {
    /*font-family: oldstandard_i;  08-08-2023 */
    font-style:italic;
}
Using oldstandard_i the italic appears also BOLD, which is not desired.

-----
Regenerate dev1 displays
cd ../
sh redo.sh 1
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/bhs.xml dev1/pywork/bhs.dtd


Note: missing ger markup in 'unmittelbare Folge' under k1=Anantarya
ertönen lassen
************************************************
08-08-2023 revisions (END)

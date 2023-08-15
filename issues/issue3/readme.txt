08-11-2023


Ref: https://github.com/sanskrit-lexicon/BHS/issues/3

german word list source:
 https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4

 copied as temp_wordlist-german.txt

german word list from spellchecker:
cp ../../eng_error_lang/spellchecker_german.txt temp_spellchecker_german.txt

french word list from spellchecker:
cp ../../eng_error_lang/spellchecker_french.txt temp_spellchecker_french.txt
remove 30 1-character lines

 
Start with:
cp /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt temp_bhs_0.txt

add 
------------------------------------------------------
check1_ger.py

Add these words to temp_wordlist-german.txt, based on Google Translate
arauf
Zuspeise
süss
Halschmuck
Thürflügel
grosse
üte
umherbewegen
Ueberbringen

python check1.py temp_bhs_0.txt ger temp_wordlist-german.txt
search for non-german words in <ger>X</ger>

Jmd
Düte
cucullus
trāyin
admonitio
Jmd
admonere
Düte
Śakti
Durgā
Jmd
balustrade

python check1.py temp_bhs_0.txt ger temp_spellchecker_german.txt

The spellchecker list is much less complete:
118 words not found!

------------------------------------------------------
Italic text with unmarked German.
  Exclude italic text starting with <ger>, <fr>, <tib>

Note: remove 1-letter 'words' in temp_spellcheck_german.txt. 22 removed.

--- Generate changes
python check2.py temp_bhs_0.txt ger temp_spellchecker_german.txt temp_change_1_ger.txt

cp temp_change_1_ger.txt change_1_ger.txt
manual edit of change_1_ger.txt
  60 lines changed.

--- apply changes
python updateByLine.py temp_bhs_0.txt change_1_ger.txt temp_bhs_1.txt
60 change transactions from change_1_ger.txt
------------------------------------------------------

------------------------------------------------------
Italic text with unmarked French.
  Exclude italic text starting with <ger>, <fr>, <tib>


--- Generate changes
python check2.py temp_bhs_1.txt fr temp_spellchecker_french.txt temp_change_2_fr.txt

cp temp_change_2_fr.txt change_2_fr.txt
manual edit of change_2_fr.txt
  
--- apply changes
python updateByLine.py temp_bhs_1.txt change_2_fr.txt temp_bhs_2.txt
42 change transactions from change_2_fr.txt

------------------------------------------------------
local install and check
cp temp_bhs_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh bhs  ../../bhs
sh xmlchk_xampp.sh bhs
# ok!

cd /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue3
------------------------------------------------------
08-13-2023
Acc. to Andhrabharati, there still remains unmarked
German, and perhaps other language, text.


Generate list of ALL unmarked italic text;
  restrict to italic text fragments which contain at
  least one word not recognized as english.

  For english word list, use temp_words_alpha.txt,
  a copy of https://github.com/dwyl/english-words/blob/master/words_alpha.txt
  
  
python check3.py temp_bhs_2.txt temp_words_alpha.txt check3.txt
1152 italic phrases identified as containing non-english.

check3_edit.txt
 Those from check3.txt that need correction (chosen manually) from check3.txt
 
python check3a_edit.py check3_edit.txt temp_check3a_edit.txt
  # reformat
 cp temp_check3a_edit.txt check3a_edit.txt
 manually make correcctions to the 'new'
 Note: 08-14-2023  Modified for 13 additional changes.
 
# generate change file
python change3.py temp_bhs_2.txt check3a_edit.txt change_3.txt
70 read from check3a_edit.txt
64 changes written to change_3.txt

# apply changes
python updateByLine.py temp_bhs_2.txt change_3.txt temp_bhs_3.txt
64 change transactions from change_3.txt

# requires change to one.dtd, so <ab> can be within <ger>
------------------------------------------------------
------------------------------------------------------
local install and check version 3
cp temp_bhs_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh bhs  ../../bhs
sh xmlchk_xampp.sh bhs
# ok!

cd /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue3
------------------------------------------------------

------------------------------------------------------

revise this BHS repository


------------------------------------------------------
TODO cdsl install
******************************************************

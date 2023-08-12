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
revise this BHS repository

------------------------------------------------------
TODO cdsl install
******************************************************

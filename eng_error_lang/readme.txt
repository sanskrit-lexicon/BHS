

For english word corrections, the final results are in files:
 bhs_error_ok.txt   Jim classified these as 'OK' for various reasons (3793)
 bhs_error_todo.txt  Jim identified these for Sampada to examine. (180)


These files were derived from bhs_error.txt in several steps.
bhs_error.txt from 
https://github.com/sanskrit-lexicon/CORRECTIONS/blob/master/english_error/output/bhs_error.txt
at commit 7b27d61e4d5

----------------------------------------------------------------
python bhsnumber.py bhs_error.txt bhs_errornum.txt
# add 4-digit sequence number for each line.
# Thus, original ordering of bhs_error.txt can be retrieved if
# the numbered records are scattered.


----------------------------------------------------------------
python marksan.py bhs_errornum.txt bhs_errornum1.txt bhs_ok_san.txt

This program uses two techniques to mark words with a classification as
 'OK' or 'TODO' and a 'reason'.  The 'TODO' cases are for Sampada to examine.
The marked words are written to file bhs_ok_san.txt (including the 'TODO')
and the unmarked to bhs_errornum1.txt.
This program is run multiple times as the classification is revised.
In the final run, all records are written to bhs_ok_san.txt, and no
records are written to bhs_errornum1.txt.
The classification methods:
There are 4075 words in bhs_errornum.txt
1. Several lists of words are developed and used by marksan program.
  180 bhs_english_edit.txt
  367 bhs_french_edit.txt
  102 bhs_german_edit.txt
   39 bhs_misc_edit.txt
  351 bhs_sanmisc_edit.txt
  137 bhs_tibet_edit.txt
 1176 total words marked by being in one of these lists.
2. Various pattern matching is done in marksan.py program
 words marked by patterns. (4075 - 1176 = 2899)

The final bhs_ok_san.txt file has all the records, with classification.
Separate into two files
 3895 bhs_error_ok.txt     The 'OK' records of bhs_ok_san.txt
  180 bhs_error_todo.txxt  The 'TODO' records
  
Remove the initial sequence number in both files.

---------------------------------------------------------------
Initial French and German word lists were developed using the
SpellChecker module.  However, these lists are not very helpful.
  Example: 'porridge' is classified as both an English and French word. Yuk!
Better lists of French/German words are needed.

Following notes for possible future reference.
python bhs_french.py temp_bhs.txt bhs_french.txt
# find all italic text phrases {%.*?%}
# find all words in a phrase, (space-separate) require the word to contain 3 characters
# Write all words recognized as French,
# (using SpellChecker module), then add ALL (long) words as French
Output distinct French words, along with frequency.

python bhs_german.py temp_bhs.txt bhs_german.txt
# find all italic text phrases {%.*?%}
# find all words in a phrase, (space-separate) require the word to contain 3 characters
# Write all words recognized as German,
# (using SpellChecker module), then add ALL (long) words as German
Output distinct German words, along with frequency.

------------------------------------------------
bhslang.py   program to dump lines with 'Tib.' (Tibetan) from digitization
of bhs.txt

python bhslang.py 'Tib.' temp_bhs.txt bhslang_tibet_raw.txt
This output was not found useful currently.

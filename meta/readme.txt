meta/readme.txt

This directory for general update of the csl-orig/v02/bhs/meta2.txt file.
It is adapted from the issues/issue1/meta directory.

The main task is to run programs to generate counts of
- extended ascii characters
- tags - mainly xml tags.

Main logic is:
- copy latest versions from csl-orig of
  - digitization (xxx.txt) and
  - meta2  (xxx-meta2.txt)
- run programs to generate statistics from xxx.txt
- manually adapt xxx-meta2.txt from these statistics
- copy revised xxx-meta2 back to csl-orig and update csl-orig.

-----------------------------------------------
cp /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs.txt temp_bhs.txt
cp  /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs-meta2.txt bhs-meta2.txt


-----------------------------------------------
python check_ea1.py temp_bhs.txt check_ea1.txt
75 extended ascii codes found in ../temp_bhs_ab_1.txt

-----------------------------------------------
python check_tags.py temp_bhs.txt check_tags.txt check_tags_local.txt

-----------------------------------------------
# revise bhs-meta2.txt manually

-----------------------------------------------

-----------------------------------------------
Regenerate displays locally
# copy revised meta2 file to csl-orig
cp bhs-meta2.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/

cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh bhs  ../../bhs
sh xmlchk_xampp.sh bhs
# ok
--------------------------------
# sync to github
--- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02
git pull # anything required to avoid collisions?
# if no collisions,
git add .
git commit -m "bhs: update meta2 file.
Ref: https://github.com/sanskrit-lexicon/BHS/issues/5"
git push
-------------------------------
# install at cologne
cd [[scans/csl-orig]]
git pull

cd ../csl-pywork/v02
grep bhs redo_cologne_all.sh
sh generate_dict.sh bhs  ../../BHSScan/2020/

-------------------------------
--- sync this repository to github
cd /c/xampp/htdocs/sanskrit-lexicon/BHS/meta
git add .
git commit -m "Revise bhs-meta2. #5"

************************************************

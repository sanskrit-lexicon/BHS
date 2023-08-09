meta/readme.txt


-----------------------------------------------
cp  /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhs-meta2.txt bhs-meta2_old.txt

cp  /c/xampp/htdocs/cologne/csl-orig/v02/gra/gra-meta2.txt temp_gra-meta2.txt

cp bhs-meta2_old.txt bhs-meta2.txt

-----------------------------------------------
python check_ea1.py ../temp_bhs_ab_1.txt check_ea1.txt
78 extended ascii codes found in ../temp_bhs_ab_1.txt

python check_tags.py ../temp_bhs_ab_1.txt check_tags.txt

-----------------------------------------------
# revise bhs-meta2.txt manually
# copy revised version to csl-orig
cp bhs-meta2.txt /c/xampp/htdocs/cologne/csl-orig/v02/bhs/

-----------------------------------------------

edit /c/xampp/htdocs/cologne/csl-orig/v02/bhs/bhsheader.xml
add:
   <editionStmt>
     <edition>xml version, <date when="2023-08-10">10 Aug 2023</date></edition>
     <respStmt>
       <resp>abbreviation markup</resp>
       <name>Mr. K. Nagabhushana Rao</name>
     </respStmt>
   </editionStmt>

-----------------------------------------------
Regenerate dev1 displays
cd ../
sh redo.sh 1
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/bhs.xml dev1/pywork/bhs.dtd



************************************************

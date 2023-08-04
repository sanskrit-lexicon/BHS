sfx="$1"
if [ ! $1 ] ; then
    echo usage "sh redo.sh N"
    exit 1
fi    
 
file=temp_bhs_ab_$sfx.txt
# filex=bhs_hwextra.txt
origdir=/c/xampp/htdocs/cologne/csl-orig/v02/bhs
orig=$origdir/bhs.txt
#origx=$origdir/$filex
echo "Copy $file to $orig"
cp $file $orig
#echo "Copy $filex to $origx"
#cp $filex $origx
echo
devdir=/c/xampp/htdocs/sanskrit-lexicon/bhs/issues/issue1/dev$sfx
echo "BEGIN Generate display in $devdir"
echo "-------------------------------------------------"
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
root=dev_$sfx
echo
pwd
sh generate_dict.sh bhs $devdir
echo
echo "END generate display in $devdir"
echo "-------------------------------------------------"

cd $origdir
echo "restoring $orig"
git restore bhs.txt
#echo "restoring $origx"
#git restore $filex


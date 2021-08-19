python hw1.py bhshw0.txt bhshw1.txt bhshw1_note.txt
# http://unix.stackexchange.com/questions/28158/is-there-a-tool-to-get-the-lines-in-one-file-that-are-not-in-another
diff -U $(wc -l < bhshw1.txt) bhshw1.txt ../../Cologne_localcopy/bhs/bhsxml/xml/bhshw1.txt | grep '^-' | sed 's/^-//g' > dhavalmodification.txt

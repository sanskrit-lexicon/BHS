# coding=utf-8
"""hw1.py  ejf July 1,2013
 June 16, 2014. Adapated for utf-8
 Read  bhshw0.txt, whose lines were created with:
 out = "%s,%s:%s:%s,%s" %(page,col,hw,l1,l2)

 'Normalize' all headword spellings, but still leave in Anglicized Sanskrit.
 Then output the same format, using the normalized headword
 Here are the normalizations:
 () remove parenthetical string
 () remove initial non-alphabetical characters
 () remove comma and all text following the comma
 () remove space and all text following the space
 () remove '-'
 () remove '?'
 () remove apostrophe (avagraha)
 () change 's\xa4' to 's4'  (occurs once)
 () change 'a\xa4' to 'a' (occurs once)
 () change '\x85yenaiva' to '' (occurs once) (ellipsis)
 () remove '(' and following characters (occurs twice)
 () convert to lower case
 () remove ending non [a-z0-9]

 Check that the remaining characters are
  a-z, 1-9
"""
import re
import sys,codecs
def hw_normalize(hw):
 hw0 = hw
 hw = re.sub(r"\(.*?\)","",hw)
 hw = re.sub(r"^[^a-zA-Z]+","",hw)
 hw = re.sub(r",.*$","",hw)
 hw = re.sub(r" .*$","",hw)
 hw = re.sub(r"-","",hw)
 hw = re.sub(r"[?]","",hw)
 hw = re.sub(r"[']","",hw)
 hw = re.sub(r"s\xa4","s4",hw)
 hw = re.sub(r"a\xa4","a",hw) # for pr2ccha¤-paripr2cchika1 = pfcCaparipfcCikA
 hw = re.sub(u"\…yenaiva","",hw)
 hw = re.sub(r"\(.*$","",hw)
 hw = hw.lower() # make lower case
 hw = re.sub(r"[^a-z0-9]$","",hw)
 hw = re.sub(r"au1","au",hw)
 m = re.search(r'([^a-z0-9])',hw)
 if m:
  c = m.group(1)
  cint = ord(c)
  print "headword '%s' (%s) has unexpected character '%s' = %s" %(hw,hw0,c,cint)
 return hw

filename=sys.argv[1] #'bhshw0.txt'
fileout =sys.argv[2] # 'bhshw1.txt'
filenote =sys.argv[3] #'bhshw1_note.txt'
f = codecs.open(filename,encoding='utf-8',mode='r')
fout = codecs.open(fileout,'w','utf-8')
fnote = codecs.open(filenote,'w','utf-8')
n = 0
nnote = 0
nout = 0 # number of headword lines written to output
for line in f:
 n = n+1
 line = line.strip() # remove starting or ending whitespace
 (pagecol,hw0,line12) = re.split(':',line)

 hw = hw_normalize(hw0)
 out = "%s:%s:%s" %(pagecol,hw,line12)
 fout.write("%s\n" % out);
 nout = nout + 1
 if ((hw != hw0) and ((hw+"-")!=hw0)):
  out = "%s:  '%s' => '%s'  :%s" %(pagecol,hw0,hw,line12)
  fnote.write("%s\n" % out);
  nnote = nnote + 1
f.close()
fout.close()
fnote.close()
print "file %s has %s lines" % (filename,n)
print "%s headwords written to file %s" % (nout,fileout)
print "%s headwords with normalization changes written to %s" % (nnote,filenote)

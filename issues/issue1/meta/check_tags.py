""" check_tags.py Assumes input is utf8-unicode, and similarly writes.
    10-17-2017. 08-08-2023 (python3)
"""
import re,sys
import codecs, unicodedata

def check_tags(filein,fileout):
# set up regex callback 'repl' with access to dictionary asdict
 asdict = {}
 # read the lines of the file
 f = codecs.open(filein,encoding='utf-8',mode='r')
 n = 0
 for line in f:
  line = line.rstrip()
  n = n + 1
  tags = re.findall(r'<.*?>',line)
  for c in tags:
   if c not in asdict:
    asdict[c] = 0
   asdict[c] = asdict[c] + 1
  
 f.close()
 keys = asdict.keys()
 print(len(keys),"tags found in",filein)
 # print "n=",n
 keys = sorted(keys)
 print(len(keys))
 outlines = []
 for key in keys:
  asobj = asdict[key]
  #key1=convert(key)
  out = "%s   %5d " %(key,asobj)
  outlines.append(out)
 fout = codecs.open(fileout,'w','utf-8')
 for out in outlines:
  fout.write("%s\n" % out)
 fout.close()
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 check_tags(filein,fileout)

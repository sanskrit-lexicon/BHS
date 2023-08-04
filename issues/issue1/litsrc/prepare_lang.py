# coding=utf-8
""" prepare_lang.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lang(fileout,d):
 abbrevs = sorted(d.keys(),key = lambda abbrev : abbrev.lower())
 outarr = []

 for abbrev in abbrevs:
  count = d[abbrev]
  tip=""
  # repla
  out = '%s:%s:%s' %(abbrev,tip,count)
  outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(abbrevs),"lines written to",fileout)
 
def count_lang(lines):
 d = {}
 n = 0
 for iline,line in enumerate(lines):
  # 
  for m in re.finditer(r'<lang>(.*?)</lang>',line):
   abbrev = m.group(1)
   if abbrev not in d:
    d[abbrev] = 0
   d[abbrev] = d[abbrev] + 1
   n = n + 1
 abbrevs = list(d.keys())
 print(len(abbrevs),"global lang tags")
 print(n,'lang tag instances found')
 return d

if __name__=="__main__":
 filein = sys.argv[1] # temp_graab
 fileout = sys.argv[2] # <lang>X</lang>
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 d = count_lang(lines)
 write_lang(fileout,d)


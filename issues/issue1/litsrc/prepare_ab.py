# coding=utf-8
""" prepare_ab.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_ab(fileout,d):
 abbrevs = sorted(d.keys(),key = lambda abbrev : abbrev.lower())
 outarr = []
 for abbrev in abbrevs:
  count = d[abbrev]
  tip=""
  out = '%s:%s:%s' %(abbrev,tip,count)
  outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(abbrevs),"lines written to",fileout)
 
def count_ab(lines):
 d = {}
 n = 0
 for iline,line in enumerate(lines):
  # 
  for m in re.finditer(r'<ab>(.*?)</ab>',line):
   abbrev = m.group(1)
   if abbrev not in d:
    d[abbrev] = 0
   d[abbrev] = d[abbrev] + 1
   n = n + 1
 abbrevs = list(d.keys())
 print(len(abbrevs),"global ab tags")
 print(n,'ab tag instances found')
 return d

class ABlocal(object):
 def __init__(self,abbrev):
  self.abbrev = abbrev
  self.dtip = {}

def count_ab1(lines):
 # local abbreviations
 d = {}
 n = 0
 for iline,line in enumerate(lines):
  # 
  for m in re.finditer(r'<ab n="(.*?)">(.*?)</ab>',line):
   abbrev = m.group(2)
   tip = m.group(1)
   if abbrev not in d:
    d[abbrev] = ABlocal(abbrev)
   rec = d[abbrev]
   dtip = rec.dtip
   if tip not in dtip:
    dtip[tip] = 0
   dtip[tip] = dtip[tip] + 1
   n = n + 1
 abbrevs = list(d.keys())
 print(len(abbrevs),"local ab tags")
 print(n,'local ab tag instances found')
 return d

def write_ab1(fileout,d):
 abbrevs = sorted(d.keys(),key = lambda abbrev : abbrev.lower())
 outarr = []

 for abbrev in abbrevs:
  rec = d[abbrev]
  #tip = rec.tip
  #count = rec.count
  #out = '%s:%s:%s' %(abbrev,tip,count)
  dtip = rec.dtip
  for tip in dtip:
   count = dtip[tip]
   out = '%s:%s:%s' %(abbrev,tip,count)
   outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(abbrevs),"lines written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # temp_graab
 fileout = sys.argv[2] # <ls>X</ls>
 fileout1 = sys.argv[3] # <ls n="Y">x</ls>
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 d = count_ab(lines)
 write_ab(fileout,d)
 d1 = count_ab1(lines)
 write_ab1(fileout1,d1)
 

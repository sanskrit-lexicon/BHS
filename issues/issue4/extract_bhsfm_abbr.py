# coding=utf-8
""" extract_bhsfm_abbr.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_rec_lines(fileout,recs):
 # recs is list of Tagcount objects
 outarr = [rec.line for rec in recs]
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)

class Tagcount:
 def __init__(self,line,iline):
  self.line = line
  parts = line.split('\t') # tab-separated values
  self.parts0 = parts
  self.status =  len(parts) == 4
  if not self.status:
   print('problem at line',iline+1)
   #print(line)
   #exit(1)
   return
  self.parts = [p.strip() for p in parts]
  self.countstr, self.lsstr,self.ls,self.tooltip = self.parts
  
def index_to_tagcount(lines):
 recs = []
 nls = 0
 nab = 0
 for iline,line in enumerate(lines):
  m = re.search(r'^(.*?)\t= (.*)$',line)
  if m == None:
   continue
  ls = m.group(1)
  tooltip = m.group(2)
  # classify as 'ls' or 'ab' based on first character of ls
  c = ls[0]
  if c.lower() == c:
   lsstr = 'ab'  # lower case assume common abbreviation
  else:
   lsstr = 'ls'  # upper case assume literary source.
  countstr = '0' # not meaningful
  newline = '\t'.join((countstr,lsstr,ls,tooltip))
  rec = Tagcount(newline,iline)
  recs.append(rec)
 return recs

if __name__=="__main__":
 filein = sys.argv[1] # BHS.Grammar_Front.pages.txt
 fileout = sys.argv[2] # file 
 lines = read_lines(filein)
 recs = index_to_tagcount(lines)
 write_rec_lines(fileout,recs)
 # stats
 nab = len([rec for rec in recs if rec.lsstr == 'ab'])
 nls = len([rec for rec in recs if rec.lsstr == 'ls'])
 print('nab=%s, nls=%s' %(nab,nls))
 

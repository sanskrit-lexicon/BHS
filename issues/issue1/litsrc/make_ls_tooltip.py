# coding=utf-8
""" make_ls_tooltip.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Tip(object):
 def __init__(self,line):
  parts = line.split('\t')
  if len(parts) != 3:
   print('error: line\n',parts)
   exit(1)
  self.abbrev,self.info,self.tip= line.split('\t')
  self.abtype,countstr,self.src = self.info.split(',')
  self.count = int(countstr)
 
def init_abbrevs(filein):
 lines = read_lines(filein)
 recs = [Tip(line) for line in lines]
 print(len(recs),"abbreviations read from",filein)
 d = {}
 for rec in recs:
  abbrev = rec.abbrev
  if abbrev in d:
   print('init_abbrev: unexpected duplicate',abbrev)
  d[abbrev] = rec
 # resolve the tooltips of form {X}
 # use d to fill in {X}
 n = 0 # count of number of such replacements
 for rec in recs:
  oldtip = rec.tip
  m = re.search(r'^\{(.*?)\}$',oldtip)
  if m == None:
   # tip not a pointer
   continue
  refabbrev = m.group(1)
  if refabbrev not in d:
   print('reference abbrev not found!',rec.line)
   exit(1)
  refrec = d[refabbrev]
  newtip = refrec.tip
  # use newtip in rec
  rec.tip = newtip
  n = n + 1
 print(" %s tooltip pointers resolved" %n)
 
 return recs,d

def write_tips(fileout,d):
 abbrevs = sorted(d.keys(),key = lambda abbrev : abbrev.lower())
 outarr = []
 no  = 0 # abbreviations with count = 0
 n = 0 # other abbreviations
 notip = 0 # instances with unknown tip
 ncount = 0 # number of instances
 notipcount = 0
 for abbrev in abbrevs:
  rec = d[abbrev]
  tip = rec.tip
  count = rec.count
  if count == 0:
   no = no + 1
   continue # don't write
  else:
   out = '%s\t%s' % (abbrev,tip)
   outarr.append(out)
   n = n + 1
   if tip == '?':
    notip = notip + 1
    notipcount = notipcount + count
   else:
    ncount = ncount + count
 # write   
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 # summary stats
 print(n,"tooltips written to",fileout)
 print(no,"front matter with no instances (not written to",fileout)
 print(ncount,"instances with an assigned tip")
 print(notip,"abbreviations with ? as tip")
 print(notipcount,"instances with ? as tip")

if __name__=="__main__":
 filein = sys.argv[1]  # match_ab_final.txt
 fileout = sys.argv[2] # tooltip file for csl-pywork
 recs,d = init_abbrevs(filein)
 write_tips(fileout,d)
 

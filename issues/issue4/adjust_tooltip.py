# coding=utf-8
""" adjust_tooltip.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_recs(fileout,recs):
 outrecs = []
 for rec in recs:
  outarr = []
  if rec.newtooltip == None:
   out = rec.line # no change
  else:
   parts0 = rec.parts0
   parts0[3] = rec.newtooltip
   out = '\t' . join(parts0)
  outarr.append(out)
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(recs),"records written to",fileout)
  

class Tagcount:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t') # tab-separated values
  self.parts0 = parts
  self.status =  len(parts) == 4
  self.parts = [p.strip() for p in parts]
  self.countstr, self.lsstr,self.ls,self.tooltip = self.parts
  assert self.lsstr in ('ls','lsfm','lsfm?')
  self.newtooltip = None

def init_tagcount(filein):
 lines = read_lines(filein)
 recs = [Tagcount(line) for line in lines]
 return recs

def generate_changes(lines):
 group = None
 for iline,line in enumerate(lines):
  m = re.search('old: (.*)$',line)
  if m != None:
   old = m.group(1)
   continue
  m = re.search('new: (.*)$',line)
  if m != None:
   new = m.group(1)
   group = (old,new)
   yield group
   old = None
  
def init_changes(filein):
 lines = read_lines(filein)
 changes = list(generate_changes(lines))
 print(len(changes),"changes read from",filein)
 return changes

def apply_changes(recs,changes):
 d = {} # make changes a dictionary
 for change in changes:
  old,new = change
  if old in d:
   print('duplicate change found')
   exit(1)
  d[old] = new
 n = 0
 for rec in recs:
  tip = rec.tooltip
  if tip in d:
   newtip = d[tip]
   rec.newtooltip = newtip
   n = n + 1
 print(n,"records with tooltip change")
 
if __name__=="__main__":
 filein = sys.argv[1] # tagcount_ls_1.txt
 filein1 = sys.argv[2] # tooltip changes
 fileout = sys.argv[3] # both files written to facilitate comparison
 #fileout1 = sys.argv[4] # change stats
 
 recs = init_tagcount(filein)
 changes = init_changes(filein1)
 apply_changes(recs,changes)  # newtooltip attribute computed
 write_recs(fileout,recs)

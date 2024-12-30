# coding=utf-8
""" compare_tagcount_ls.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_diffs_check3(fileout,diffs):
 outrecs = []
 for idiff,diff in enumerate(diffs):
  outarr = []
  rec1,rec2,irec = diff
  outarr.append('; diff %s at line %s' %(idiff+1,irec+1))
  outarr.append('; cdsl')
  outarr.append(rec1.line)
  outarr.append('; anna')
  outarr.append(rec2.line)
  outarr.append('; ------------------------------------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(diffs),"difference records written to",fileout)

def write_compare(fileout,recs1,recs2):
 outrecs = []
 for irec,rec1 in enumerate(recs1):
  rec2 = recs2[irec]
  assert rec1.parts[0:-1] == rec2.parts[0:-1]
  a1 = [rec1.countstr,rec1.lsstr,rec1.ls]
  outarr = []
  assert ':' not in rec1.ls
  assert ':' not in rec2.ls
  
  # x is a 'status' field
  if rec1.tooltip == rec2.tooltip:
   x = '=='
  elif rec2.tooltip.startswith(';;'):
   x = ';;'
   if rec1.tooltip.startswith('?'):
    x = x + '?'
  elif rec1.tooltip.startswith('?'):
   #assert rec2.tooltip == rec2.tooltip
   x = '_?'
  else:
   x = ''
  a1.append(x)
  a = ':'.join(a1)
  # a = '%s:%s:%s' % (a,x)
  outarr.append(a)
  outarr.append('anna: %s' % rec2.tooltip)
  if rec1.tooltip != rec2.tooltip:
   outarr.append(';')
   outarr.append('cdsl: %s' % rec1.tooltip)
  #else:
  # outarr.append('cdsl: %s' % 'SAME')
  outarr.append('; ------------------------------------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(recs1),"records written to",fileout)
 
class Tagcount:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t') # tab-separated values
  self.parts0 = parts
  self.status =  len(parts) == 4
  self.parts = [p.strip() for p in parts]
  self.countstr, self.lsstr,self.ls,self.tooltip = self.parts
  assert self.lsstr in ('ls','lsfm','lsfm?')
  
def init_tagcount(filein):
 lines = read_lines(filein)
 recs = [Tagcount(line) for line in lines]
 return recs

def check1(recs):
 recs1 = [rec for rec in recs if rec.status == False]
 print(len(recs1),"records with wrong number of fields")
 for irec,rec in enumerate(recs):
  if rec.status == False:
   print('line %s has %s parts' %(irec+1,len(rec.parts)))
   for ipart,part in enumerate(rec.parts):
    print('part[%s] = %s' %(ipart+1,rec.parts[ipart]))
def check2(recs1,filein1,recs2,filein2):
 print('%s has %s records' % (filein1,len(recs1)))
 check1(recs1)
 print('%s has %s records' % (filein2,len(recs2)))
 check1(recs2)

def check3(recs1,recs2):
 n = 0
 diffs = []
 for irec,rec1 in enumerate(recs1):
  rec2 = recs2[irec]
  if ((rec1.countstr == rec2.countstr) and
      (rec1.lsstr == rec2.lsstr) and
      (rec1.ls == rec2.ls)):
   pass
  else:
   n = n + 1
   diff = (rec1,rec2,irec)
   diffs.append(diff)
   if False:
    print('check3 difference at line %s' % (irec+1,))
    print(rec1.line)
    print(rec2.line)
 print('check3 finds %s problems' %n)
 return diffs

if __name__=="__main__":
 filein = sys.argv[1] # tagcount_ls_0.txt (cdsl)
 filein1 = sys.argv[2] # tagcount_ls_anna_0.txt
 fileout = sys.argv[3] # both files written to facilitate comparison
 
 recs1 = init_tagcount(filein)
 recs2 = init_tagcount(filein1)
 check2(recs1,filein,recs2,filein1)
 assert len(recs1) == len(recs2)
 diffs_check3 = check3(recs1,recs2)
 if diffs_check3 != []:
  write_diffs_check3(fileout,diffs_check3)
 else:
  write_compare(fileout,recs1,recs2)
 

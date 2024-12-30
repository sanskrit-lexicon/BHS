# coding=utf-8
""" mark_lsfm.py
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

def write_recs(fileout,recs):
 outarr= []
 for rec in recs:
  fields = (rec.countstr, rec.lsstr,rec.ls,rec.tooltip) 
  line = '\t'.join(fields)
  outarr.append(line)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)

def write_recs(fileout,recs):
 outarr= []
 for rec in recs:
  fields = (rec.countstr, rec.lsstr,rec.ls,rec.tooltip) 
  line = '\t'.join(fields)
  outarr.append(line)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)

def write_diffs(fileout,diffs):
 outrecs= []
 for idiff,diff in enumerate(diffs):
  rec,recfm = diff
  outarr = []
  outarr.append('; diff %s:' % (idiff+1))
  outarr.append('; tagcount %s:%s:%s' %(rec.countstr, rec.lsstr,rec.ls))
  outarr.append(';    front %s:%s:%s' %(recfm.countstr, recfm.lsstr,recfm.ls))
  outarr.append('; tagcount:')
  outarr.append(rec.tooltip)
  outarr.append(';    front:')
  outarr.append(recfm.tooltip)
  outarr.append('; ------------------------------------------------------')
  outrecs.append(outarr)
 
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"diffs written to",fileout)
 
class Tagcount:
 def __init__(self,line,iline):
  self.line = line
  parts = line.split('\t') # tab-separated values
  self.parts0 = parts
  self.status =  len(parts) == 4
  if not self.status:
   print('problem at line',iline+1)
   for ic,c in enumerate(line):
    print(ic,c)
   
   print('line=',line)
   print('cccc', len(parts))
   exit(1)
   return
  self.parts = [p.strip() for p in parts]
  self.countstr, self.lsstr,self.ls,self.tooltip = self.parts

def init_tagcount(filein):
 lines = read_lines(filein)
 recs = []
 for iline,line in enumerate(lines):
  rec = Tagcount(line,iline)
  recs.append(rec)
 return recs

def recsfm_dict(recsfm):
 d = {}
 for rec in recsfm:
  if rec.lsstr == 'ab':
   continue # filter out normal abbreviations
  key = rec.ls
  if key in d:
   print('recsfm_dict duplicate key',key)
  d[key] = rec
 return d

def adjust_lsstr(recs,recsfm):
 fmd = recsfm_dict(recsfm)
 n = 0
 n1 = 0
 diffs = [] # returned
 for rec in recs:
  key = rec.ls  
  if key in fmd:
   recfm = fmd[key]
   assert recfm.lsstr == 'ls'
   # do a check on tooltip
   if recfm.tooltip == rec.tooltip:
    rec.lsstr = 'lsfm'
   else:
    rec.lsstr = 'lsfm?'
    n1 = n1 + 1
    diff = (rec,recfm)
    diffs.append(diff)
   n = n + 1
 print('adjust_lsstr changed %s records' %n)
 print('%s of these with different tooltips' % n1)
 return diffs

if __name__=="__main__":
 filein = sys.argv[1] # bhsfm_abbr
 filein1 = sys.argv[2] # tagcount_ls_0
 fileout = sys.argv[3] # tagcount_ls_1
 fileout1 = sys.argv[4]
 print(filein)
 recsfm = init_tagcount(filein)
 print(filein1)
 recs = init_tagcount(filein1)
 print('diffs')
 diffs = adjust_lsstr(recs,recsfm)
 write_recs(fileout,recs)
 if len(diffs) != 0:
  write_diffs(fileout1,diffs)
 else:
  print('no diffs to print')
 
 #nab = len([rec for rec in recs if rec.lsstr == 'ab'])
 #nls = len([rec for rec in recs if rec.lsstr == 'ls'])
 #print('nab=%s, nls=%s' %(nab,nls))
 

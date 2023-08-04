# coding=utf-8
""" match_ls.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class LS(object):
 def __init__(self,lstype,line,iline):
  self.line = line
  self.lstype = lstype
  parts = line.split(':')
  assert len(parts) == 3
  self.abbrev = parts[0]
  self.tip = parts[1]
  assert self.tip == ''  # will be filled in later
  self.count = int(parts[2])

class FR(object):
  def __init__(self,line):
   self.line = line
   parts = line.split('\t')
   try:
    assert len(parts) == 3
   except:
    print('FR init error:',line)
    exit(1)
   self.src = parts[0]
   self.abbrev = parts[1]
   temp = parts[2]
   m = re.search(r'^= (.*)$',temp)
   self.tip = m.group(1)
   self.used = 0  # number of times used in matching
   
def init_lsrecs_unused(filein):
 recs = []
 lines = read_lines(filein)
 # get 'type' of abbreviation from filename
 # blah_TYPE.txt
 m = re.search(r'_([^._]*?)[.]txt',filein)
 lstype = m.group(1)
 n = 0 # aggregate rec.count
 for iline,line in enumerate(lines):
  rec = LS(lstype,line,iline)
  recs.append(rec)
  n = n + rec.count
 print('%s lsrecs of type %s from %s' %(len(recs),lstype,filein))
 print(n,"total extract count")
 return recs

def init_lsrecs(filein):
 recs = []
 lines = read_lines(filein)
 # get 'type' of abbreviation from filename
 # blah_TYPE.txt
 m = re.search(r'_([^._]*?)[.]txt',filein)
 lstype = m.group(1)
 n = 0 # aggregate rec.count
 for iline,line in enumerate(lines):
  rec = LS(lstype,line,iline)
  recs.append(rec)
  n = n + rec.count
 print('%s lsrecs of type %s from %s' %(len(recs),lstype,filein))
 print(n,"total extract count")
 return recs

def init_front(filein):
 recs = []
 lines = read_lines(filein)
 for iline,line in enumerate(lines):
  recs.append(FR(line))
 print('%s front records from %s' %(len(recs),filein))
 d = {}
 n = 0
 for rec in recs:
  abbrev = rec.abbrev
  if abbrev in d:
   n = n + 1
   print('init_front duplicate:',abbrev)
   recold = d[abbrev]
   print('   old tip:',recold.tip)
   print('   new tip:',rec.tip)
  else:
   d[abbrev] = rec
 print('init_front finds %s duplicates in %s' %(n,filein))
 return d

def check_dups(lsrecs):
 d = {}
 n = 0 # number of duplicates
 for rec in lsrecs:
  abbrev = rec.abbrev
  if abbrev in d:
   print('check_dups found dup abbrev: "%s"' % abbrev)
   recold = d[abbrev]
   print('  OLD  %s %s' % (recold.lstype,recold.line))
   print('  NEW  %s %s' % (rec.lstype,rec.line))
   n = n + 1
  else:
   d[abbrev] = rec
 print('check_dups found %s duplicate abbrevations' % n)

def match(recs,dfront):
 n = 0 # number of recs matched
 ni = 0 # number of instances
 for rec in recs:
  abbrev = rec.abbrev
  if abbrev in dfront:
   recfr = dfront[abbrev]
   rec.tip = recfr.tip
   recfr.used = recfr.used + 1
   ni = ni + rec.count
   n = n + 1
 print('match: finds tooltips for %s records (%s instances)' % (n,ni))

def write_1(fileout,lsrecs):
 outarr = []
 for rec in lsrecs:
  if rec.tip == '':
   # no match found
   out = rec.line
   outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"unmatched extracts written to",fileout)
 
def write_2(fileout,lsrecs):
 outarr = []
 for rec in lsrecs:
  if rec.tip == '':
   # no match found
   out = 'FR1\t%s\t= ' % rec.abbrev
   outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"unmatched extracts written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # front_ls
 fileout = sys.argv[2] # match_ls.txt
 fileout1 = sys.argv[3]  # temp_front_work.txt
 lsrecs = []
 for filename in sys.argv[4:]:
  arecs = init_lsrecs(filename)
  for arec in arecs:
   lsrecs.append(arec)
 print(len(lsrecs),' # lsrecs')
 check_dups(lsrecs)
 dfront = init_front(filein)
 match(lsrecs,dfront)  # update lsrecs and dfront
 write_1(fileout,lsrecs)
 write_2(fileout1,lsrecs)
 

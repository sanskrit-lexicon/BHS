# coding=utf-8
""" match_ab_final.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class AB(object):
 def __init__(self,abtype,line,iline):
  self.line = line
  self.abtype = abtype
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
   assert len(parts) == 3
   self.src = parts[0]
   self.abbrev = parts[1]
   temp = parts[2]
   m = re.search(r'^= (.*)$',temp)
   self.tip = m.group(1)
   self.used = 0  # number of times used in matching
   
def init_abrecs(filein):
 recs = []
 lines = read_lines(filein)
 # get 'type' of abbreviation from filename
 # blah_TYPE.txt
 m = re.search(r'_([^._]*?)[.]txt',filein)
 abtype = m.group(1)
 for iline,line in enumerate(lines):
  recs.append(AB(abtype,line,iline))
 print('%s abrecs of type %s from %s' %(len(recs),abtype,filein))
 return recs

def init_abrecs(filein):
 recs = []
 lines = read_lines(filein)
 # get 'type' of abbreviation from filename
 # blah_TYPE.txt
 m = re.search(r'_([^._]*?)[.]txt',filein)
 abtype = m.group(1)
 for iline,line in enumerate(lines):
  recs.append(AB(abtype,line,iline))
 print('%s abrecs of type %s from %s' %(len(recs),abtype,filein))
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

def check_dups(abrecs):
 d = {}
 n = 0 # number of duplicates
 for rec in abrecs:
  abbrev = rec.abbrev
  if abbrev in d:
   print('check_dups found dup abbrev: "%s"' % abbrev)
   recold = d[abbrev]
   print('  OLD  %s %s' % (recold.abtype,recold.line))
   print('  NEW  %s %s' % (rec.abtype,rec.line))
   n = n + 1
  else:
   d[abbrev] = rec
 print('check_dups found %s duplicate abbrevations' % n)

def match(recs,dfront):
 n = 0 # number of recs matched
 for rec in recs:
  abbrev = rec.abbrev
  if abbrev in dfront:
   recfr = dfront[abbrev]
   rec.tip = recfr.tip
   recfr.used = recfr.used + 1
   n = n + 1
 print('match: finds tooltips for %s records' % n)

def write(fileout,abrecs,dfront):
 dab = {}
 ndup = 0
 print('write:',len(abrecs),' # abrecs')

 for rec in abrecs:
  abbrev = rec.abbrev
  if abbrev in dab:
   print('write: duplicate abbrev merged',abbrev)
   ndup = ndup + 1
   recold = dab[abbrev]
   # update count
   newcount = rec.count + recold.count
   recold.count = newcount
   newabtype = '%s/%s' %(recold.abtype,rec.abtype)
   recold.abtype = newabtype
  else:
   dab[abbrev] = rec

 print('write: %s duplicate abbreviations' % ndup)
 dabkeys = sorted(dab.keys(),key = lambda abbrev: abbrev.lower())
 print('write: %s merged abbreviations' % len(dabkeys))
 nusedtot = 0
 for abbrev in dfront:
  recfr = dfront[abbrev]
  nused = recfr.used
  if nused not in (0,1):
   print('front record for "%s" used %s times' %(abbrev,nused))
  if nused != 0:
   nusedtot = nusedtot + 1
 print('nusedtot = ',nusedtot)
 assert nusedtot == len(dabkeys)
 # begin generating outarr
 outarr = []
 for abbrev in dabkeys:
  rec = dab[abbrev]
  if rec.tip == '':
   print('ERROR: write: no tooltip for abbrev "%s"' %rec.abbrev)
   exit(1)
  abbrev = rec.abbrev
  recfr = dfront[abbrev]
  abtype = rec.abtype
  count = rec.count
  countstr = str(count)
  tipsrc = recfr.src
  tip = rec.tip
  assert tip == recfr.tip
  out = '%s\t%s,%s,%s\t%s' % (abbrev,abtype,countstr,tipsrc,tip)
  outarr.append(out)
 # send outarr to file
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"pre-tooltip records written to",fileout)
 
def write_unused_fr(fileout,dfront):
 keys = sorted(dfront.keys(),key = lambda abbrev: abbrev.lower())
 outarr = []
 for abbrev in keys:
  recfr = dfront[abbrev]
  if recfr.used == 0:
   out = '%s\t%s\t%s' %(recfr.abbrev,recfr.src,recfr.tip)
   outarr.append(out)
 # send outarr to file
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"unused front-matter abbreviations written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] # front_ab
 fileout = sys.argv[2] # match_ab.txt
 fileout1 = sys.argv[3] # unused records
 abrecs = []
 for filename in sys.argv[4:]:
  arecs = init_abrecs(filename)
  for arec in arecs:
   abrecs.append(arec)
 print(len(abrecs),' # abrecs')
 check_dups(abrecs)
 dfront = init_front(filein)
 match(abrecs,dfront)  # update abrecs and dfront
 write(fileout,abrecs,dfront)
 write_unused_fr(fileout1,dfront)
 

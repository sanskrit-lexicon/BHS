# coding=utf-8
""" match_ls_final.py
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
   assert len(parts) == 3
   self.src = parts[0]
   self.abbrev = parts[1]
   temp = parts[2]
   m = re.search(r'^= (.*)$',temp)
   self.tip = m.group(1)
   self.used = 0  # number of times used in matching

def init_lsrecs(filein):
 recs = []
 lines = read_lines(filein)
 # get 'type' of abbreviation from filename
 # blah_TYPE.txt
 m = re.search(r'_([^._]*?)[.]txt',filein)
 lstype = m.group(1)
 for iline,line in enumerate(lines):
  recs.append(LS(lstype,line,iline))
 print('%s lsrecs of type %s from %s' %(len(recs),lstype,filein))
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
 ##### the rest of this code will be in make_ab_tooltip.py
 #
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
 print("init_front: %s tooltip pointers resolved" %n)
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

def unused_match(recs,dfront):
 n = 0 # number of recs matched
 for rec in recs:
  abbrev = rec.abbrev
  if abbrev in dfront:
   recfr = dfront[abbrev]
   rec.tip = recfr.tip
   recfr.used = recfr.used + 1
   n = n + 1
 print('match: finds tooltips for %s records' % n)

class LSFR(object):
 def __init__(self,abbrev,recls,recfr):
  self.abbrev = abbrev
  if recls != None:
   self.lstype = recls.lstype # always ls
   self.count = recls.count
  else:
   self.lstype = 'ls'
   self.count  = 0
  if recfr != None:
   self.src = recfr.src  # FR0 or FR1
   self.tip = recfr.tip
   self.used = recfr.used
  else:
   self.src = 'FR2'
   self.tip = ''
   self.used = 0
  self.recls = recls
  self.recfr = recfr
  
def merge(dls,dfront):
 # first, get all keys (abbrev) in either dictionary
 keysls = set(dls.keys())  # instances from extract_ls
 keysfr = set(dfront.keys()) # instances from front_ls
 keysall = keysls.union(keysfr)
 dall = {}
 recsall = []
 for abbrev in keysall:
  if abbrev in keysls:
   recls = dls[abbrev]
  else:
   recls = None
  if abbrev in keysfr:
   recfr = dfront[abbrev]
  else:
   recfr = None
  rec = LSFR(abbrev,recls,recfr)
  recsall.append(rec)
  assert abbrev not in dall
  dall[abbrev] = rec
 return dall
 """
 for rec in recsall:
  abbrev = rec.abbrev
  recls = rec.recls
  recfr = rec.recfr
  if recfr != None:
   recfr = dfront[abbrev]
   rec.tip = recfr.tip
   recfr.used = recfr.used + 1
   
 print('match: finds tooltips for %s records' % n)
 """
 
def lsrecs_dict(lsrecs):
 dls = {}
 ndup = 0
 print('write:',len(lsrecs),' # lsrecs')

 for rec in lsrecs:
  abbrev = rec.abbrev
  if abbrev in dls:
   print('write: duplicate abbrev merged',abbrev)
   ndup = ndup + 1
   recold = dls[abbrev]
   # update count
   newcount = rec.count + recold.count
   recold.count = newcount
   newlstype = '%s/%s' %(recold.lstype,rec.lstype)
   recold.lstype = newlstype
  else:
   dls[abbrev] = rec
 return dls

def write(fileout,dall):
 allkeys = sorted(dall.keys(),key = lambda abbrev: abbrev.lower())
 print('write: %s merged abbreviations' % len(allkeys))
 nusedtot = 0
 for abbrev in dall:
  rec = dall[abbrev]
  nused = rec.used
  if nused not in (0,1):
   print('front record for "%s" used %s times' %(abbrev,nused))
  if nused != 0:
   nusedtot = nusedtot + 1
 print('nusedtot = ',nusedtot)
 #if nusedtot != len(dlskeys):
 # print('write WARNING: nusedtot=%s, number of dlskeys=%s' %(nusedtot,len(dlskeys)))
 # exit(1)
 # begin generating outarr
 outarr = []
 for abbrev in allkeys:
  rec = dall[abbrev]
  if rec.tip == '':
   pass
  #recfr = dfront[abbrev]
  lstype = rec.lstype
  count = rec.count
  countstr = str(count)
  tipsrc = rec.src
  tip = rec.tip
  #assert tip == recfr.tip
  out = '%s\t%s,%s,%s\t%s' % (abbrev,lstype,countstr,tipsrc,tip)
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
 filein = sys.argv[1] # front_ls
 filein1 = sys.argv[2] # extract_ls
 fileout = sys.argv[3] # match_ls_final.txt
 #fileout1 = sys.argv[3] # unused records
 lsrecs = init_lsrecs(filein1)
 check_dups(lsrecs)
 dls = lsrecs_dict(lsrecs)
 # 
 dfront = init_front(filein)
 dall = merge(dls,dfront)  # update lsrecs and dfront
 write(fileout,dall)
 # write_unused_fr(fileout1,dfront)
 

# coding=utf-8
""" textdiff_count.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def get_metafield(f,meta):
 if f == 'k2':
  if '<h>' in meta:
   regex = r'<%s>(.*?)<' % f
  else:
   regex = r'<%s>(.*?)$' % f
 else:
  regex = r'<%s>(.*?)<' % f
 m = re.search(regex,meta)
 value = m.group(1)
 return value


def entries_compare(entries1,entries2):
 ndiff = 0 # number of entries with remaining differences
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  assert len(e1.datalines) == len(e2.datalines)
  diff = False
  for iline,line1 in enumerate(e1.datalines):
   line2 = e2.datalines[iline]
   if line1 != line2:
    diff = True
  if diff:
   ndiff = ndiff + 1
   if ndiff == 1:
    print('first diff at',e1.metaline)
 print(ndiff,"entries are different")
    
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt cdsl
 filein1 = sys.argv[2] # bhs.txt AB
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 entries_compare(entries_cdsl,entries_ab)
 

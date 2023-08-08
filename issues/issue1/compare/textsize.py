# coding=utf-8
""" textsize.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines
 
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


def hwdiffs(cdsl_lines,ab_lines):
 cdsl_metas = [line for line in cdsl_lines if line.startswith('<L>')]
 ab_metas = [line for line in ab_lines if line.startswith('<L>')]
 print('cdsl has %s entries' % len(cdsl_metas))
 print('ab   has %s entries' % len(ab_metas))
 assert len(cdsl_metas) == len(ab_metas)
 diffs = []
 for iline,line in enumerate(cdsl_metas):
  line1 = ab_metas[iline]
  if line != line1:
   diff = (line,line1)
   diffs.append(diff)
 print(len(diffs),"differences in metalines")
 return diffs

def textsize(entries):
 d = {}  # number of entries with given text size (rounded to hundred chars)
 n = 0 # number of entries 
 for entry in entries:
  n = n + 1
  text = ' '.join(entry.datalines)
  entry.textsize = len(text)
  # text size to nearest hundred characters
  m  = round (entry.textsize // 100)
  entry.textsize_h = m
  if m not in d:
   d[m] = 0
  d[m] = d[m] + 1
 keys = d.keys()
 keys = sorted(keys)
 ncum = 0
 for m in keys:
  n1 = d[m]
  ncum = ncum + n1
  pct = round((ncum * 100) / n)
  print(m,n1,pct)
 
def write_big(fileout,entries):
 outarr = []
 for i,entry in enumerate(entries):
  m = entry.textsize_h
  if m < 10:
   continue
  k1 = entry.metad['k1']
  # textsize is 1000+ characters
  outarr.append('%s %s' %(k1,m))
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')
 print(len(outarr),'long entries written to',fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #bhs.txt AB
 fileout = sys.argv[2] #

 entries = digentry.init(filein)

 textsize(entries)
 write_big(fileout,entries)
 
 

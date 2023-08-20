# coding=utf-8
""" tagcount.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Tip(object):
 def __init__(self,line):
  self.line = line
  try:
   self.abbrev,self.tipdata = line.split('\t')
  except:
   print('Tip format error:',line)
   exit(1)
  self.used = 0
  self.tags = []  # filled in tips_in_line

def init_tooltips(filein,option):
 lines = read_lines(filein)
 recs = [Tip(line) for line in lines]
 print(len(recs),'Tooltips from',filein)
 return recs

def tips_in_line(d,line,tags,meta):

 for m in re.finditer(r'<(.*?)>(.*?)</\1>',line):
  tag = m.group(1)
  if ' ' in tag:
   # not interested tags with attributes
   continue
  if tag not in tags:
   continue
  abbrev = m.group(2)
  if abbrev not in d:
   print('unknown: "%s"' %abbrev)
  else:
   rec = d[abbrev]
   rec.used = rec.used + 1
   if tag not in rec.tags:
    rec.tags.append(tag)
    
   
def update_tips(entries,tips,tags):
 d = {}
 for rec in tips:
  abbrev = rec.abbrev
  if abbrev in d:
   print('duplicate tip:',abbrev)
   exit(1)
  d[abbrev] = rec

 for ientry,entry in enumerate(entries):
  for iline,line in enumerate(entry.datalines):
   tips_in_line(d,line,tags,entry.metaline)

def unused_tips(tips):
 n = 0
 for rec in tips:
  if rec.used == 0:
   n = n + 1
   print('unused: ',rec.line)
 print(n,"tips are unused")

def write_tipcounts(tips):
 outarr = []
 for rec in tips:
  if rec.tags == []:
   tagstr = '_'
  else:
   tagstr = '/'.join(rec.tags)
  abbrev = rec.abbrev.ljust(15)
  out = '%4s\t%s\t%s\t%s' %(rec.used,tagstr,abbrev,rec.tipdata)
  outarr.append(out)

 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"tip counts written",fileout)


if __name__=="__main__":
 option = sys.argv[1]  # ab or ls
 if option == 'ab':
  tags = ['ab','lang','ed','lex','ms']
 elif option == 'ls':
  tags = ['ls']
 else:
  print('unknown option:',option)
  exit(1)
 filein = sys.argv[2] # bhs.txt cdsl
 filein1 = sys.argv[3] # tooltip file
 fileout = sys.argv[4] #
 entries = digentry.init(filein)
 tips = init_tooltips(filein1,option)
 update_tips(entries,tips,tags)
 unused_tips(tips)
 write_tipcounts(tips)


# coding=utf-8
""" check_lat.py

"""
from __future__ import print_function
import sys, re,codecs

class Change(object):
 def __init__(self,lnum,line,meta,texts):
  self.lnum = lnum
  self.line = line
  self.meta = meta
  self.texts = texts
  
def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_changes(fileout,changes):
 outrecs = []
 for rec in changes:
  outarr = []
  outarr.append('; %s' % rec.meta)
  line = rec.line  # old line
  newline = line
  for itext,text in enumerate(rec.texts):
   oldtext = '{%' + text + '%}'
   #newtext0 = '<%s>%s</%s>' %(lang,text,lang)
   #newtext = '{%' + newtext0 + '%}'
   #newline = newline.replace(oldtext,newtext)
   outarr.append('; old: %s' %oldtext)
   #outarr.append('; new: %s' %newtext)
   outarr.append('; -----')
  lnum = rec.lnum
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  #outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; --------------------------------------------------------')
  outrecs.append(outarr)
 # write outrecs
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"changes written to",fileout)

def write_corrs(fileout,corrs):
 outrecs = []
 for rec in corrs:
  outarr = []
  outarr.append('old: %s' % rec.old)
  outarr.append('new: %s' % rec.new)
  outarr.append(';')
  outrecs.append(outarr)
 # write outrecs
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"corrections written to",fileout)

class CORR(object):
 def __init__(self,old,new):
  self.old = old
  self.new = new
  
def get_corrs(lines):
 nfound = 0
 regexraw = r'<lat>(.*?)</lat>'
 regex = re.compile(regexraw)
 corrs = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   meta = line
   continue
  if line.startswith('<LEND>'):
   meta = None
   continue
  texts = []  # texts which should be changed
  for m in re.finditer(regex,line):
   oldtext = m.group(0)
   body = m.group(1)
   newtext = '<bot>%s</bot>' % body
   corrs.append(CORR(oldtext,newtext))
 print(len(corrs),"texts marked for change")
 return corrs
 
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt
 fileout = sys.argv[2] # unmarked italic
 lines = read_lines(filein)
 corrs = get_corrs(lines)
 write_corrs(fileout,corrs)
 

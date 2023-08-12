# coding=utf-8
""" check2.py

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

def write_changes(fileout,changes,lang):
 outrecs = []
 for rec in changes:
  outarr = []
  outarr.append('; %s' % rec.meta)
  line = rec.line  # old line
  newline = line
  for itext,text in enumerate(rec.texts):
   oldtext = '{%' + text + '%}'
   newtext0 = '<%s>%s</%s>' %(lang,text,lang)
   newtext = '{%' + newtext0 + '%}'
   newline = newline.replace(oldtext,newtext)
   outarr.append('; old: %s' %oldtext)
   outarr.append('; new: %s' %newtext)
   outarr.append('; -----')
  lnum = rec.lnum
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; --------------------------------------------------------')
  outrecs.append(outarr)
 # write outrecs
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"changes written to",fileout)

def init_lang(filein):
 d = {}
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   word = line.rstrip('\r\n')
   d[word] = True
 print(len(d))
 return d

import string

punctuation = string.punctuation + '…‘°’'
def get_words(text):
    '''The function should take one argument which is a string'''
    return text.translate(str.maketrans('', '', punctuation)).split()

#print(get_words('Hello world, my name is...James!'))

def check_lang(lines,dlang,lang):
 nfound = 0
 regexraw = r'{%(.*?)%}' 
 regex = re.compile(regexraw)
 langstart = ('<ger>','<fr>','<tib>')
 changes = [] # list of Change objects
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   meta = line
   continue
  if line.startswith('<LEND>'):
   meta = None
   continue
  texts = []  # texts which should be changed
  for m in re.finditer(regex,line):
   text = m.group(1)
   if text.startswith(langstart):
    continue
   words = get_words(text)
   for word in words:
    if word in dlang:
     found = True
    elif word.lower() in dlang:
     found = True
    else:
     found = False
    if found: # an error situation.
     print(word,text)
     nfound = nfound + 1
     texts.append(text)
     break # no need to check further words
  # prepare changes
  if texts != []:
   lnum = iline + 1
   change = Change(lnum,line,meta,texts)
   changes.append(change)
 print('nfound=',nfound)
 print(len(changes),"lines to change")
 return changes
 
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt
 lang = sys.argv[2]  # ger
 filedict = sys.argv[3] # list of lang words
 fileout = sys.argv[4] # change file
 dlang = init_lang(filedict)
 lines = read_lines(filein)
 changes = check_lang(lines,dlang,lang)
 write_changes(fileout,changes,lang)
 

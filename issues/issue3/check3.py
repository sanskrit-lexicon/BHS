# coding=utf-8
""" check3.py

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

def write_changes_1(fileout,changes):
 outrecs = []
 for rec in changes:
  outarr = []
  #outarr.append('; %s' % rec.meta)
  line = rec.line  # old line
  newline = line
  for itext,text in enumerate(rec.texts):
   oldtext = '{%' + text + '%}'
   outarr.append('%s' %oldtext)
   #outarr.append('; new: %s' %newtext)
  lnum = rec.lnum
  #outarr.append('%s old %s' %(lnum,line))
  #outarr.append(';')
  #outarr.append('%s new %s' %(lnum,newline))
  #outarr.append('; --------------------------------------------------------')
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
 print(len(d),'words found in',filein)
 return d

import string

punctuation = string.punctuation + '…‘°’'
def get_words(text):
 '''The function should take one argument which is a string'''
 text1 = text.replace('-',' ')
 text1 = text1.replace('ʼs',' ')
 text1 = text1.lower()
 words = text1.translate(str.maketrans('', '', punctuation)).split()
 #if '-' in text:
 # print('dbg',text)
 # print(words)
 # exit(1)
 return words

#print(get_words('Hello world, my name is...James!'))

def check_italic(lines,dlang):
 nfound = 0
 regexraw = r'{%(.*?)%}' 
 regex = re.compile(regexraw)
 langstart = ('<ger>','<fr>','<tib>','<lat>')
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
    # text is already marked as a language
    continue
   words = get_words(text)
   found = False
   for word in words:
    if word not in dlang:
     found = True
     break
    elif word.lower() not in dlang:
     found = True
     break
   # 
   if found: # text has non-english word
    #print(word,text)
    #exit(1)
    texts.append(text)
  # prepare changes
  if texts != []:
   nfound = nfound + len(texts)
   lnum = iline + 1
   change = Change(lnum,line,meta,texts)
   changes.append(change)
 print('nfound=',nfound)
 print(len(changes),"lines to change")
 return changes
 
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt
 fileeng = sys.argv[2]  # english word list
 fileout = sys.argv[3] # unmarked italic
 lines = read_lines(filein)
 deng = init_lang(fileeng)
 changes = check_italic(lines,deng)
 # write_changes(fileout,changes)
 write_changes_1(fileout,changes)
 

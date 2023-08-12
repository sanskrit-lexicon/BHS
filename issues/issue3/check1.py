# coding=utf-8
""" check1.py

"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_2(fileout,abrecs):
 outarr = []
 for rec in abrecs:
  if rec.tip == '':
   # no match found
   out = 'FR1\t%s\t= ' % rec.abbrev
   outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"unmatched extracts written to",fileout)

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


def check_lang(lines,dlang,lang):
 nok = 0
 nprob = 0
 regexraw = r'<%s>(.*?)</%s>' %(lang,lang)
 regex = re.compile(regexraw)
 for line in lines:
  if line.startswith('<L>'):
   meta = line
   continue
  if line.startswith('<LEND>'):
   meta = None
   continue
  for m in re.finditer(regex,line):
   text = m.group(1)
   words = get_words(text)
   for word in words:
    if word in dlang:
     nok = nok + 1
     #print('ok:',word)
    elif word.lower() in dlang:
     nok = nok + 1
    else:
     nprob = nprob + 1
     if word == 'ie':
      print('%s: %s'  %(word,text))
     else:
      print(word)
 print('nok=%s, nprob=%s' %(nok,nprob))
 
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt
 lang = sys.argv[2]  # ger
 filedict = sys.argv[3] # list of german words
 dlang = init_lang(filedict)
 lines = read_lines(filein)
 dfound = check_lang(lines,dlang,lang)

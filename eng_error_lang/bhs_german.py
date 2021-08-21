#-*- coding:utf-8 -*-
"""bhs_german
 
"""
import sys,re,codecs
from spellchecker import SpellChecker

def spellcheckWords(lang):
 checker = SpellChecker(language=lang)
 s = set(checker.word_frequency.keys())
 print(len(s),"spellcheck words for language",lang)
 return s
englishwords = spellcheckWords('en')
germanwords = spellcheckWords('de')

def spellchecker_wordlist(fileout,langwords):
 with codecs.open(fileout,encoding='utf-8',mode='w') as f:
  n =0
  for word in langwords:
   if not word in englishwords:
    f.write(word+'\n')
    n = n + 1
 print(n,"words written to",fileout)

#spellchecker_wordlist('spellchecker_german.txt',germanwords)
#exit(1)
def isGerman(word):
 isgerman = (word in germanwords)
 isenglish = (word in englishwords)
 return (isgerman and (not isenglish))

def parseheadline(headline):
 """<L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>2"""
 headline = headline.strip()
 splits = re.split('[<]([^>]*)[>]([^<]*)',headline)
        #print(splits)
 result = {}
 for i in range(len(splits)):
  if i % 3 == 1:
   result[splits[i]] = splits[i+1]
 return result

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  #  extra attributes
  self.langlines = []
  self.langflag = False
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

def notify_out(metaline,lnum,line):
 outarr = []
 outarr.append('; %s'%metaline)
 outarr.append('%s old %s' %(lnum,line))
 outarr.append(';')
 return outarr

def change_out(metaline,lnum,line,new):
 outarr = []
 outarr.append('; %s'%metaline)
 outarr.append('%s old %s' %(lnum,line))
 outarr.append('%s new %s' %(lnum,new))
 outarr.append(';')
 return outarr

def find_german_words(entry,d):
 for line in entry.datalines:
  for m in re.finditer(r'{%(.*?)%}',line):
   phrase = m.group(1)
   words = re.split(r' +',phrase)
   found = False
   words1 = [w for w in words if len(w)>=3]
   words2 = [w for w in words1 if isGerman(w)]
   
   for word in words2:
    if word not in d:
     d[word] = 0
    d[word] = d[word] + 1
    
def write(fileout,d):
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0 # number of entries with langcode
  keys = sorted(d.keys())
  for key in keys:
   out = '%s %s' %(key,d[key])
   n = n + 1
   f.write(out+'\n')
 print(n,"German distinct words identified in",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 #regexraw1 = r'{#[^#]*?([a-zA-Z0-9\^\\]+[~][\^\\/]+[a-zA-Z0-9]*)'  

 #print(regexraw1)
 #regex1 = re.compile(regexraw1)

 entries = init_entries(filein)
 d = {}  # dictionary of French words, with frequency
 
 for entry in entries:
  find_german_words(entry,d)
 
 write(fileout,d)

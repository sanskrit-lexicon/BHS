#-*- coding:utf-8 -*-
"""bhsnumber.py
 
"""
import sys,re,codecs

class Entry(object):
 def __init__(self,line):
  self.line = line
  self.seq,self.L,self.k1,self.word = line.split(':')
  self.mark = None

def init_entries(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [Entry(line.rstrip('\r\n')) for line in f]
 print(len(recs),"Records from",filein)
 return recs

def readwords(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  d = {}
  for line  in f:
   line = line.rstrip('\r\n')
   parts = re.split(r' +',line)
   word = parts[0]
   if word in d:
    print('duplicate word %s in %s' %(word,filein))
   d[word]=True
 return d

def mark_french(entries,filein):
 d = readwords(filein)
 for entry in entries:
  if entry.mark != None:
   continue
  if entry.word in d:
   entry.mark = 'french'
   
def mark_german(entries,filein):
 d = readwords(filein)
 for entry in entries:
  if entry.mark != None:
   continue
  if entry.word in d:
   entry.mark = 'german'

def mark_tibet(entries,filein):
 d = readwords(filein)
 for entry in entries:
  if entry.mark != None:
   continue
  if entry.word in d:
   entry.mark = 'tibet'

def mark_misc(entries,filein):
 d = readwords(filein)
 for entry in entries:
  if entry.mark != None:
   continue
  if entry.word in d:
   entry.mark = 'misc'

def mark_sanmisc(entries,filein):
 d = readwords(filein)
 for entry in entries:
  if entry.mark != None:
   continue
  if entry.word in d:
   entry.mark = 'sanmisc'

def mark_english(entries,filein):
 d = readwords(filein)
 print(len(d.keys()),"English words in",filein)
 for entry in entries:
  if entry.mark != None:
   continue
  if entry.word in d:
   entry.mark = 'english'

def mark_ending(entries):
 sanendings = ('ati','ate','anti','ante','ena','iya','eti','asya','ti',
            'ala','to','ehi','am','ana','avya','antu',
            'aiva','eva','ir','asi','ase','ya','esi','tum',
               'aka','ika','hi','ye','ara','eha','et','eta',
               'min','ah','nty','ita','tva','ec','emi','o','ed')
 tibendings = ('ug','ig','og','eg','ag') #tibet
 for entry in entries:
  if entry.mark != None:
   continue
  for ending in sanendings:
   if entry.word.endswith(ending):
    mark = 'san-'+ending
    entry.mark = mark
    break
  for ending in tibendings:
   if entry.word.endswith(ending):
    mark = 'tib-'+ending
    entry.mark = mark
    break
   
def mark_beginning(entries):
 sanbegins = ('pra','sam','adhi','anu','abhi','upa','ava','vi',
              'nir','pari',)
 tibbegins = ('rk','sg','sb','gz','gl','rn','bz','sp','sm',
              'gd','bg') # tibetan
 for entry in entries:
  if entry.mark != None:
   continue
  for begin in sanbegins:
   if entry.word.startswith(begin):
    mark = '-san'+begin
    entry.mark = mark
    break
  for begin in tibbegins:
   if entry.word.startswith(begin):
    mark = '-tib'+begin
    entry.mark = mark
    break
   
def mark_miscending(entries):
 endings = ('ur')
 for entry in entries:
  if entry.mark != None:
   continue
  for ending in endings:
   if entry.word.endswith(ending):
    mark = 'misc-'+ending
    entry.mark = mark

def mark_substring(entries):
 sansubstrings = ('cc','jj','dd','tt','mm','ss','pp',
               'bhy',
               'ai', # contains some non-sanskrit words (akai, etc.)
                  'dharm','garb',
                  'bh','dh','gg')
 tibsubstrings = ('zh', 'bs','dz',# tibetan 
                     )
 for entry in entries:
  if entry.mark != None:
   continue
  for substring in sansubstrings:
   if substring in entry.word:
    mark = 'san-'+substring
    entry.mark = mark
    break
  for substring in tibsubstrings:
   if substring in entry.word:
    mark = 'tib-'+substring
    entry.mark = mark
    break
                  
def write_unmarked(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for entry in entries:
   if entry.mark == None:
    out = entry.line
    f.write(out + '\n')
    n = n + 1
 print(n,"records written to",fileout)
 
def write_marked(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  d = {} # count of marks
  for entry in entries:
   if entry.mark == None:
    continue
   if entry.mark == 'english':
    out = "%s:TODO:%s" %(entry.line,entry.mark)
   else:
    out = "%s:OK:%s" %(entry.line,entry.mark)
   f.write(out + '\n')
   n = n + 1
   if entry.mark not in d:
    d[entry.mark] = 0
   d[entry.mark] = d[entry.mark] + 1
 print(n,"records written to",fileout)
 keys = sorted(d.keys())
 for key in keys:
  print(d[key],key)

if __name__=="__main__":
 filein = sys.argv[1] #  bhs_errornum
 fileout1 = sys.argv[2] # unmarked
 fileout2 = sys.argv[3] # marked
 entries = init_entries(filein)
 mark_english(entries,'bhs_english_edit.txt')  # words to check, mostly english
 mark_french(entries,'bhs_french_edit.txt')
 mark_german(entries,'bhs_german_edit.txt')
 mark_tibet(entries,'bhs_tibet_edit.txt')
 mark_misc(entries,'bhs_misc_edit.txt')
 mark_sanmisc(entries,'bhs_sanmisc_edit.txt')
 mark_miscending(entries)
 mark_ending(entries)
 mark_beginning(entries)
 mark_substring(entries)  # sanskrit, tibetan
 write_unmarked(fileout1,entries)
 write_marked(fileout2,entries)

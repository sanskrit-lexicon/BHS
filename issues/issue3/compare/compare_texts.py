# coding=utf-8
""" compare_texts.py
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

def write_diffs(fileout,diffs):
 #exit(1)
 outrecs = []
 for idiff,diff in enumerate(diffs):
  cdsl_meta,ab_meta = diff
  outarr = []
  L = get_metafield('L',cdsl_meta)
  L1 = get_metafield('L',ab_meta)
  assert L == L1
  pc_cdsl = get_metafield('pc',cdsl_meta)
  pc_ab   = get_metafield('pc',ab_meta)
  assert pc_cdsl == pc_ab
  k1_cdsl = get_metafield('k1',cdsl_meta)
  k1_ab   = get_metafield('k1',ab_meta)
  assert k1_cdsl == k1_ab
  k2_cdsl = get_metafield('k2',cdsl_meta)
  k2_ab   = get_metafield('k2',ab_meta)
  assert k2_cdsl != k2_ab
  
  outarr.append('; %03d: L=%s' %(idiff+1,L))
  outarr.append('cdsl: %s' % cdsl_meta)
  outarr.append('  ab: %s' % ab_meta)
  outarr.append(';  ------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(diffs),"differences written to",fileout)
 
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

def check_ab_bodycount(entries):
 #
 n = 0 # number of entries 
 for entry in entries:
  if len(entry.datalines) != 1:
   print(entry.metaline,' has ',len(entry.datalines),'lines')
   n = n + 1

def remove_markup(x):
 x = re.sub('\[Page.*?\]',' ',x)
 for markup in ('¦', '{@','@}','{%','%}','〔','〕',
                '<ab>','</ab>','<ls>','</ls>',
                '<lang>','</lang>', '<hom>','</hom>',
                '<lex>','</lex>','<tib>','</tib>',
                ';', ',', '…', '—','-',']','[',')','(' ):
  x = x.replace(markup,' ')
 x = re.sub(r'[.:]',' ',x)
 x = re.sub(r'<ab.*?>',' ',x)  # <ab n="t">
 x = re.sub(r'<ls.*?>',' ',x)  # <ls n="t">
 """
 x = re.sub(r'[(] +', '(',x)
 x = re.sub(r' +[)]' ,')',x)
 x = re.sub(r'\[ +','[',x)
 x = re.sub(r' /]',']',x)
 """
 x = re.sub(r'  +',' ',x)
 x = x.strip()
 return x

def text_adjust_1(lines):
 # get the text:
 text = ''
 # handle line-breaks
 newlines = []
 for iline,line in enumerate(lines):
  line = line.replace('{%','') # must do this before '-' logic below
  line = line.replace('%@','')
  line = line.replace('{@','')
  line = line.replace('%}','')
  if line.endswith('-'):
   newline = line[0:-1]  # drop final '-'
  else:
   newline = line + ' ' # note last line will have extra ' '
  newlines.append(newline)
 text0 = ''.join(newlines)
 text1 = remove_markup(text0)
 return text1

def text_adjust(entries):
 for entry in entries:
  entry.text = text_adjust_1(entry.datalines)

def write(fileout,e1s,e2s):
 outrecs = []
 n = 0
 no = 0
 for i,e1 in enumerate(e1s):
  e2 = e2s[i]
  if e1.text == e2.text:
   n = n + 1
  else:
   no = no + 1
   if no < 5:
    print(e1.metaline)
    print('cdsl text\n',e1.text)
    print()
    print('ab text\n',e2.text)
   
 print(n,'entries have same text')

def compare_lines(lnum,line1,line2):
 a1 = re.split(r'\b',line1)
 a2 = re.split(r'\b',line2)
 if a1 == a2:
  return a1,a2
 # diff
 n1 = len(a1)
 n2 = len(a2)
 n = max(n1,n2)
 tok = ''
 for i in range(0,n):
  if i < n1:
   x1 = a1[i]
  else:
   x1 = None
  if i < n2:
   x2 = a2[i]
  else:
   x2 = None
  if x1 == x2:
   tok = tok + x1
  else:
   # first diff
   print(lnum)
   tok0 = tok[-20:]
   t1 = tok0 + x1
   t2 = tok0 + x2

   print(t1)
   print(t2)
   break
 return a1,a2

def compare(entries1,entries2):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  assert len(e1.datalines) == len(e2.datalines)
  for iline,line1 in enumerate(e1.datalines):
   line2 = e2.datalines[iline]
   if line1 == line2:
    # no differences
    continue
   lnum = e1.linenum1 + iline + 1
   (a1,a2) = compare_lines(lnum,line1,line2)
   if a1 != a2:
    nd = nd + 1
    #print('ntag=',ntag)
    exit(1)
   ntag = ntag + len(a1)
 print(nd,'differences in "%s" tag' % tag)
 print(ntag,'instances of "%s" tag' % tag)
 
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt cdsl
 filein1 = sys.argv[2] # bhs.txt AB
 fileout = sys.argv[3] #
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 compare(entries_cdsl,entries_ab)
 

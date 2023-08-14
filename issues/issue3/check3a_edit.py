# coding=utf-8
""" check3a_edit.py

"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write(fileout,lines):
 outrecs = []
 for line in lines:
  outarr = []
  if line.startswith(';'):
   outarr.append('; *****************************************************************************************')
   outarr.append(line)
   outarr.append('; *****************************************************************************************')
  else:
   outarr.append('old: %s' % line)
   outarr.append('new: %s' % line)
   outarr.append(';')
  outrecs.append(outarr)
 # write outrecs
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"changes written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # check3_edit
 fileout = sys.argv[2] # reformat
 lines = read_lines(filein)
 write(fileout,lines)
 

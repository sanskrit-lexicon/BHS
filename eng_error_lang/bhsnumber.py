#-*- coding:utf-8 -*-
"""bhsnumber.py
 
"""
import sys,re,codecs

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # add 0-padded sequence number so original order avail

 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0 # number of entries with langcode
  for iline,line in enumerate(lines):
   out = '%04d:%s' %(iline+1,line)
   f.write(out+'\n')

#! /usr/bin/python
import os,sys
os.system ('clear')

#file copy with commandline args

with open(sys.argv[1]) as fo1, open(sys.argv[2],'w') as fo2:
	s=fo1.read()
	fo2.write(s)





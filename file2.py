#! /usr/bin/python
import os,sys
os.system ('clear')

#new way
with open('myfile1','w') as fo:
	print 'enter data'
	s=sys.stdin.read()
	fo.write(s)




#! /usr/bin/python
import os,sys
os.system ('clear')

#reading a file
with open('myfile','r') as fo:
	s=fo.read()
	sys.stdout.write(s)




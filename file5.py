#! /usr/bin/python
import os,sys,time
os.system ('clear')

#file copy
with open('myfile') as fo1, open('xmyfile','w') as fo2:
	s=fo1.read()
	fo2.write(s)





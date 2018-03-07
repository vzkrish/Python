#! /usr/bin/python
import os,re
os.system ('clear')

with open('testfile') as fo:
	for m in fo:
		p=re.search('^#',m)
		if p:
			print m,


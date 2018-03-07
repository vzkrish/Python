#! /usr/bin/python
import os,re
os.system ('clear')

with open('testfile1') as fo:
	for m in fo:
		p=re.search('^[A-Z][0-9]',m)
		if p:
			print m,


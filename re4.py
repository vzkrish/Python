#! /usr/bin/python
import os,re
os.system ('clear')

with open('testfile1') as fo:
	for m in fo:
		p=re.match('abcd',m,re.I)
		if p:
			print m,

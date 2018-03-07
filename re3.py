#! /usr/bin/python
import os,re
os.system ('clear')
with open('data','r') as fo:
	t='([A-Z]+) ([0-9]+)-([0-9]+) ([a-z]+)'
	s=re.compile(t)
	re.purge()
	for x in fo:
		m=re.search(s,x)
		if m:
			print m.group(1,4)


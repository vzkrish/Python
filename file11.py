#! /usr/bin/python
import os,json
os.system ('clear')

with open('data1','r') as fo:
	d=json.load(fo)

for m,n in sorted(d.iteritems()):
	print '%s => %s' % (m,n)


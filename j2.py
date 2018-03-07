#! /usr/bin/python
import os,json
os.system ('clear')
with open('myp1','r') as fo:
	x=json.load(fo)

for m in x:
	print m



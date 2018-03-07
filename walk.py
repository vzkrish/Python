#! /usr/bin/python
import os
os.system ('clear')

for root,dirs,files in os.walk('./t1'):
	print root
	for m in files:
		print root+'/'+m
	print

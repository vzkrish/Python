#! /usr/bin/python
import os,filecmp
os.system ('clear')

# to check two files are identical or not
m=raw_input('enter first file name ')
n=raw_input('enter second file name ')
if filecmp.cmp(m,n):
	print 'identical files'
else:
	print 'files are different'


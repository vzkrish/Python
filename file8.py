#! /usr/bin/python
import os
os.system ('clear')

with open('myfile') as fo:
	print 'the name of the file ', fo.name
	print 'the mode of the file ', fo.mode
	print 'the file is closed ', fo.closed
print 'the file is closed ', fo.closed


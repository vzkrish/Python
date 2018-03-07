#! /usr/bin/python
import os
os.system ('clear')

n=raw_input('enter a name ')
if os.path.isfile(n) and n[-3:]=='.py':
	print '%s is a python file ' % (n)
	s=os.path.getsize(n)
	print '%s has %d bytes' % (n,s)
else:
	print 'some other entry'

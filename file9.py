#! /usr/bin/python
import os
os.system ('clear')

with open('myfile','r+') as fo:
	print 'byte no. file open %d' % (fo.tell())
	s=fo.read(20)
	t=s.upper()
	print 'byte no.  %d' % (fo.tell())
	fo.seek(-20,1)
	print 'byte no. %d' % (fo.tell())
	fo.write(t)	




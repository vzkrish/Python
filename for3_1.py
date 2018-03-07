#! /usr/bin/python
import os,glob
os.system ('clear')

#display sum of the sizes of all python files
x=glob.glob('*.py')
s=0
for m in x:
	t=os.path.getsize(m)
	s+=t
print 'total size is %d bytes' % (s)


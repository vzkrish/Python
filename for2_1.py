#! /usr/bin/python
import os
os.system ('clear')

#display sum of the sizes of all python files
x=os.listdir('.')
s=0
for m in x:
	if os.path.isfile(m) and m[-3:]=='.py':
		t=os.path.getsize(m)
		s+=t
print 'total size is %d bytes' % (s)


#! /usr/bin/python
import os
os.system ('clear')

#function definition
def abc():
	'my first function'
	k=1
	while k<3:
		print 'python'
		k+=1
	return

print 'working with user functions'
abc()		#function call
print 'DONE'
print abc.__doc__
l=abc
l()
del abc
l()

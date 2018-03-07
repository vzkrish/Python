#! /usr/bin/python
import os
os.system ('clear')

def abc(a,*b,**z):
	print a
	for j in b:
		print j
	for m,n in sorted(z.iteritems()):
		print m,n
	return

abc(12,1,2,3,x=13,y=34,z=45)


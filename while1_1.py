#! /usr/bin/python
import os
os.system ('clear')
k=1
n=5
while k<=12:
	print '%d * %d = %d' % (k,n,k*n)
	k+=1
print '\n\n\n'
k=1
n=5
while True:
	print '%d * %d = %d' % (k,n,k*n)
	k+=1
	if k>12:
		break


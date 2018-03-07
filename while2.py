#! /usr/bin/python
import os
os.system ('clear')
n=int(raw_input('enter a number '))
k=1
while k<n:
	r=n%k
	if r==0:
		q=n/k
		print '%d * %d' % (k,q)
	k+=1
	if k>q:
		break


#! /usr/bin/python
import os
os.system ('clear')
k=100
print k

def abc():
	k=200
	print k
	global m
	m=k+globals()['k']
	print m
	print locals()
	globals()['k']=1000
	return
abc()
print k
print globals()
print m

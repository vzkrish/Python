#! /usr/bin/python
import os
os.system ('clear')

def abc(x,y):
	temp=x
	x=y
	y=temp
	print x,y
	return

def pqr(z):
	z.append(100)
	print z
	return
m=100
n=200
print m,n
abc(m,n)
print m,n

a=[1,2,3]
print a
pqr(a)
print a


#! /usr/bin/python
import os
os.system ('clear')

class A(object):
	def __init__(self,a):
		self.d=a
	def __add__(self,other):
		self.d.update(other.d)
		return self.d


e={'x':1,'y':2,'z':3}
f={'m':5,'n':6,'o':7}
v1=A(e)
v2=A(f)
v3=v1+v2
print v3

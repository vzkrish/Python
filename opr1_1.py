#! /usr/bin/python
import os
os.system ('clear')

class vector(object):
	def __init__(self,a,b):
		self.first=a
		self.last=b
	def __str__(self):
		return "vector(%d,%d)" % (self.first,self.last)
	def __add__(self,other):
		return vector(self.first+other.first, self.last+other.last)

v1=vector(2,-5)
v2=vector(-7,6)
print v1+v2

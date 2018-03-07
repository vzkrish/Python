#! /usr/bin/python
import os
os.system ('clear')

#constructor and destructor
class temp(object):
	def __init__(self,a,b):
		self.eno=a
		self.ename=b
	def output(self):
		print self.eno, self.ename

	def __del__(self):
		print self.__class__.__name__, ' object destroyed'
x=temp(100,'abc')
x.output()
#del x



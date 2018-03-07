#! /usr/bin/python
import os
os.system ('clear')

#constructor and destructor
class temp(object):
	def __init__(self,a,b):
		self.__eno=a
		self.__ename=b
		self.__output()
	def __output(self):
		print self.__eno, self.__ename

x=temp(100,'abc')
#x.output()
#print x.__eno, x.__ename


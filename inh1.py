#! /usr/bin/python
import os
os.system ('clear')

#single inheritance
class A(object):
	def __init__(self):
		self.eno=111
		self.ename='computer'
class B(A):
	def output(self):
		print self.eno, self.ename

x=B()
x.output()


#! /usr/bin/python
import os
os.system ('clear')

#hierarchical inheritance
class A(object):
	def __init__(self):
		self.eno=111
		self.ename='computer'
class B(A):
	def xout(self):
		print 'B class'
		print self.eno, self.ename
class C(A):
	def xout(self):
		print 'C class'
		print self.eno, self.ename

class D(B,C):
	def abc(self):
		print 'you are in D'

x=D()
x.xout()
C.xout(x)

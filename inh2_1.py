#! /usr/bin/python
import os
os.system ('clear')

#multilevel inheritance
class A(object):
	def __init__(self):
		self.eno=111
		self.ename='computer'
class B(A):
	def xin(self):
		self.ecity='hyd'
		self.edsgn='mgr'
class C(B):
	def xout(self):
		print self.eno, self.ename
		print self.ecity, self.edsgn

x=C()
x.xin()
x.xout()

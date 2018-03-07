#! /usr/bin/python
import os
os.system ('clear')

#multiple   inheritance
class A(object):
	def __init__(self):
		self.eno=111
		self.ename='computer'
class B(object):
	def __init__(self):
		self.eno=222    
		self.ename='keyboard'
class C(B,A):
	def xout(self):
		A.__init__(self)
		print self.eno, self.ename

x=C()
x.xout()



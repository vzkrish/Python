#! /usr/bin/python
import os
os.system ('clear')

#hierarchical inheritance
class A(object):
	def __init__(self):
		self.eno=111
		self.ename='computer'
class B(A):
	def xdisplay(self):
		print 'B class'
		print self.eno, self.ename
class C(A):
	def xout(self):
		print 'C class'
		print self.eno, self.ename


x=B()
x.xdisplay()

y=C()
y.xout()



#! /usr/bin/python
import os
os.system ('clear')

class A(object):
	'This is about class'
	def __init__(self):
		self.eno=111
	def output(self):
		print self.eno

x=A()
print x.__class__.__name__
print A.__doc__
print A.__dict__
print A.__module__

print
print

print hasattr(x,'eno')
print getattr(x,'eno')
setattr(x,'eno',222)
print getattr(x,'eno')
setattr(x,'ename','computer')
print getattr(x,'ename')
delattr(x,'eno')
print getattr(x,'eno')

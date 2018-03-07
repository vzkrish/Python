#! /usr/bin/python
import os
os.system ('clear')

# class creation
class temp(object):
	k=0
	def xyz(self):
		self.eno=raw_input('enumber ')
		self.ename=raw_input('ename ')
	def pqr(self):
		print self.eno, self.ename

x=temp()
x.xyz()
x.pqr()



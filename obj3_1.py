#! /usr/bin/python
import os
os.system ('clear')

# class creation
class temp(object):
	k=0
	def xyz(self):
		self.eno=raw_input('enter number ')
		self.ename=raw_input('enter name ')
		print self.eno, self.ename

x=temp()
x.xyz()


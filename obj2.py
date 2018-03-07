#! /usr/bin/python
import os
os.system ('clear')

# class creation
class temp(object):
	eno=111
	@classmethod
	def abc(cls):
		print cls.eno
	def xyz(self):
		temp.abc()
		self.xno=222
		self.xname='computer'
		print 'you are in xyz'
		print self.xno, self.xname

x=temp()
x.xyz()


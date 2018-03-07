#! /usr/bin/python
import os
os.system ('clear')

def abc():
	print 'you are in outside function'
	def pqr():
		print 'you are in inside function'
		return
	pqr()
	return

abc()

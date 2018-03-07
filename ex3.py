#! /usr/bin/python
import os
os.system ('clear')

class myerror(Exception):
	pass

class valsmall(myerror):
	pass

class vallarge(myerror):
	pass

while True:
	try:
		n=int(raw_input('enter a value '))
		if n<100:
			raise valsmall
		elif n>100:
			raise vallarge
		elif n==100:
			break
		else:
			raise ValueError
	except valsmall:
		print 'less than 100 value'
	except vallarge:
		print 'more than 100 value'
	except ValueError:
		print 'wrong data'


	

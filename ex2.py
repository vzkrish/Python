#! /usr/bin/python
import os,sys
os.system ('clear')
try:
	n=int(raw_input('enter a number '))
	if n<10:
		raise TypeError
except ValueError:
	print 'wrong input'
except TypeError:
	print 'wrong types'
except ImportError:
	print 'no such module'
except:
	print 'other errors'
finally:
	print 'done'

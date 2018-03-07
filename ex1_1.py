#! /usr/bin/python
import os,sys
os.system ('clear')
try:
	n=int(raw_input('enter a number '))
except:
	print 'wrong input'
	print sys.exc_info()[0]
k=1
while k<=2:
	print 'python'
	k+=1


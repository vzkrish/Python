#! /usr/bin/python
import os
os.system ('clear')

# to check palindrome or not
n=raw_input('enter a name ')
m=n[::-1]
if cmp(m,n)==0:
	print 'palindrome'
else:
	print 'different'


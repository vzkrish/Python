#! /usr/bin/python
import os,datetime
os.system ('clear')
z=datetime.datetime.now()
p=z.hour
if p<12:
	print 'Good Morning'
elif p<17:
	print 'Good Afternoon'
elif p<21:
	print 'Good Evening'
else:
	print 'Good Night'


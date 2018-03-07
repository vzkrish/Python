#! /usr/bin/python
import os
os.system ('clear')

#count no. of files and dirs 
x=os.listdir('/home')
fc=0
dc=0
for m in x:
	m='/home/'+m
	if os.path.isfile(m):
		fc+=1
	elif os.path.isdir(m):
		dc+=1
	
print '%d files and %d dirs' % (fc,dc)


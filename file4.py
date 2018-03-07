#! /usr/bin/python
import os,sys,time
os.system ('clear')

# iterating thru the file
with open('myfile','r') as fo:
	for m in fo:
		sys.stdout.write(m)
		time.sleep(2)





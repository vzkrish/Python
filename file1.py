#! /usr/bin/python
import os,sys
os.system ('clear')

#create a file from the keyboard

#create a file object
fo=open('myfile','w')

#read from the keyboard into a string
print 'enter data'
s=sys.stdin.read()

#write the string into the file
fo.write(s)

#close the file object
fo.close()



#! /usr/bin/python
import os
os.system ('clear')
d={}
k=1
while k<=3:
	eno=raw_input('enter enumber ')
	ename=raw_input('enter ename ')
	ecity=raw_input('enter ecity ')
	d[eno]=[ename,ecity]
	k+=1
print d


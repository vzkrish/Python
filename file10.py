#! /usr/bin/python
import os,json
os.system ('clear')

emp={}
k=1
while k<=3:
	eno=raw_input('enter enumber ')
	ename=raw_input('enter ename ')
	ecity=raw_input('enter ecity ')
	emp[eno]=[ename,ecity]
	k+=1
print emp
with open('data1','w') as fo:
	json.dump(emp,fo)

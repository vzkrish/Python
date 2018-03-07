#! /usr/bin/python
import os
os.system ('clear')
x=[]
k=0
while k<2:
	m=[]
	l=0
	while l<3:
		n=int(raw_input('enter a value '))
		m.append(n)
		l+=1
	x.append(m)
	k+=1
print x

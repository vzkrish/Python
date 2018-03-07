#! /usr/bin/python
import os
os.system ('clear')

#create an empty list
n=[]

#run a loop to accept 10 names into n
k=1
while k<=10:
	s=raw_input('enter name ')
	n.append(s)
	k+=1

#create a set of unique names
m=set(n)

#display the names and their count
for p in m:
	print '%s => %d' % (p, n.count(p))




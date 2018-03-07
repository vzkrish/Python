#! /usr/bin/python
import os
os.system ('clear')

#function with variable length args
def abc(*p):
	return sum(p)

r1=abc()
print r1

r2=abc(1,2,3)
print r2

r3=abc(1,2,3,4,5,6,7,8,8)
print r3


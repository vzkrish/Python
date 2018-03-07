#! /usr/bin/python
import os
os.system ('clear')

def arm(n):
	s=n
	t=0
	while s!=0:
		r=s%10
		t=t+(r**3)
		s=s/10
	if n==t:
		return n



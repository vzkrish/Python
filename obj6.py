#! /usr/bin/python
import os, pickle
os.system ('clear')
from xyz import temp
with open('empdata','r') as fo:
	data=pickle.load(fo)

k=0
while k<3:
	data[k].tempout()
	k+=1


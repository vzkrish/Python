#! /usr/bin/python
import os,json
os.system ('clear')
x=[[1,2,3],[4,5,6],[7,8,9]]
with open('myp1','w') as fo:
	json.dump(x,fo)


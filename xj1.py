#! /usr/bin/python
import os,json
os.system ('clear')
x=[[1,2,3],[4,5,6],[7,8,9]]
y=json.dumps(x)

with open('myp2','w') as fo:
	fo.write(y)


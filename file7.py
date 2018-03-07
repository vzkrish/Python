#! /usr/bin/python
import os,sys
os.system ('clear')

a=['this\n','is\n','my file\n']
with open('newfile','w') as fo:
	fo.writelines(a)





#! /usr/bin/python
import os, pickle
os.system ('clear')

# class creation
class temp(object):
	k=0
	def tempin(self):
		self.eno=raw_input('enumber ')
		self.ename=raw_input('ename ')
	def tempout(self):
		temp.k+=1
		print temp.k, self.eno, self.ename

# create an array of objects
data=[]
k=1
while k<=3:
	data.append(temp())
	k+=1

#accept values
k=0
while k<3:
	data[k].tempin()
	k+=1
k=0
while k<3:
	data[k].tempout()
	k+=1

with open('empdata','w') as fo:
	pickle.dump(data,fo)

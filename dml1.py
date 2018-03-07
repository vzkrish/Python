#! /usr/bin/python
import os,MySQLdb
os.system ('clear')

#connect to the database
x=MySQLdb.connect('localhost','root','computer','verizon')

#cursor object
y=x.cursor()

data=[]
n=int(raw_input('enter no of records '))
k=1
while k<=n:
	eno=int(raw_input('enter enumber '))
	ename=raw_input('enter ename ')
	m=(eno,ename)
	data.append(m)
	k+=1
#sql statement
s="insert into vz values (%s,%s)"

#executemany
y.executemany(s,data)

#commit and close
x.commit()
x.close()

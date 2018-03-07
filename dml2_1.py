#! /usr/bin/python
import os,MySQLdb
os.system ('clear')

#connect to the database
x=MySQLdb.connect('localhost','root','computer','verizon')

#cursor object
y=x.cursor()

#selecting the rows
s='select * from vz'
y.execute(s)
p=y.fetchall()

print 'printing the records'
for m in p:
	print m
x.close()


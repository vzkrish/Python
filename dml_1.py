#! /usr/bin/python
import os,MySQLdb
os.system ('clear')

#connect to the database
x=MySQLdb.connect('localhost','root','computer','verizon')

#cursor object
y=x.cursor()

#inserting records
s1='insert into vz values (100,"abcd")'
s2='insert into vz values (101,"pqrs")'
s3='insert into vz values (102,"wxyz")'

y.execute(s1)
y.execute(s2)
y.execute(s3)
x.commit()
#close the connection
x.close()

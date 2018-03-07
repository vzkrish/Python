#! /usr/bin/python
import os,MySQLdb
os.system ('clear')

#connect to the database
x=MySQLdb.connect('localhost','root','computer','verizon')
if x:
	print 'database connection successful'

#create a cursor object from connection object
y=x.cursor()

#sql statement
s='create table vz (eno integer(10), ename character(11))'

#pass sql statement to the cursor object
y.execute(s)

#close the connection
x.close()


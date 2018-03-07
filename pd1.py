#! /usr/bin/python
import os,pandas as pd
os.system ('clear')
import openpyxl

d={}
k=1
while k<=2:
	key=raw_input('enter key ')
	l=1
	x=[]
	while l<=3:
		s=raw_input('enter name ')
		x.append(s)
		l+=1
	d[key]=x
	k+=1

df=pd.DataFrame(d)
print df

#writing to csv file
df.to_csv('mycsv1.csv',sep='\t',encoding='utf-8')

#writing to excel file
p=pd.ExcelWriter('myexcel1.xlsx',engine='openpyxl')
df.to_excel(p,sheet_name='Sheet1')
p.save()


#! /usr/bin/python
import os,openpyxl,csv
os.system ('clear')

#create a csv file
fo=open('mycsv.csv','wb')
p=csv.writer(fo,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL)


#create a workbook object
x=openpyxl.load_workbook('mysheet.xlsx')
y=x['Sheet1']
for m in y.max_row:
	z=[]
	for n in m:
		z.append(n.value)
	p.writerow(z)

fo.close()



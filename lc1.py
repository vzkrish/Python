#! /usr/bin/python
import os
os.system ('clear')
x=['monitor','keyboard','cdrom','memory','disk','cpu','http']

print x
for m in x:
	if len(m)>5:
		print m

s=[m for m in x if len(m)>5]
print s

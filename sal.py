#! /usr/bin/python
import os
os.system ('clear')

# program to compute salary
basic=int(raw_input('enter basic '))
hra=.4*basic
da=.2*basic
gross=(basic+hra+da)
ded=.1*gross
net=gross-ded
print 'basic =	%.2f,	hra =  %.2f' % (basic,hra)
print 'da = %.2f,	 	gross = %.2f' % (da,gross)
print 'ded = %.2f		net = %.2f' % (ded,net)


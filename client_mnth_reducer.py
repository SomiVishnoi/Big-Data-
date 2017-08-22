#!/usr/bin/python2
import os
import commands
import cgi,re,sys
print "Content-Type: text/html"
print
j=0
f=0
m=0
a=0
ma=0
ju=0
jl=0
au=0
s=0
o=0
n=0
d=0
for i in sys.stdin:
	if i == 'jan':
		j+=1
	if i == 'feb':
		f+=1
	if i == 'mar':
		m+=1
	if i == 'apr':
		a+=1
	if i == 'may':
		ma+=1
	if i == 'jun':
		ju+=1
	if i == 'jul':
		jl+=1
	if i == 'aug':
		au+=1
	if i == 'sept':
		s+=1
	if i == 'oct':
		o+=1
	if i == 'nov':
		n+=1
	if i == 'dec':
		d+=1
print "jan :" + j +"\n"	
print "feb :" + f +"\n"	
print "mar :" + m +"\n"	
print "apr :" + a +"\n"	
print "may :" + ma +"\n" 	
print "jun :" + ju+"\n"	
print "jul :" + jl +"\n"	
print "aug :" + au +"\n"	
print "sept :" + s +"\n"	
print "oct :" + o +"\n"	
print "nov :" + n +"\n"	
print "dec :" + d +"\n"	

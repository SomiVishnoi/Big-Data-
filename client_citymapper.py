#!/usr/bin/python2
import os
import commands
import cgi,re,sys
print "Content-Type: text/html"
print

for i in sys.stdin:
	j=i.strip()
	j[16] == 'IND':
		print i
	

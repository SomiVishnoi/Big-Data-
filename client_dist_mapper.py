#!/usr/bin/python2

import os
import commands
import cgi,re,sys

print "Content-Type: text/html:"
print 

for i in sys.stdin:
	j=i.strip()
	if j[18] >= 500 :
		print i

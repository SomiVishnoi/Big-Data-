#!/usr/bin/python2

import os
import commands
import cgi,re,sys

print "Content-Type: text/html:"
print 

count=0
for i in sys.stdin:
	count+=1
print count 

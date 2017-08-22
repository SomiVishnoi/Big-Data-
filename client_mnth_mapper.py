#!/usr/bin/python2
import os
import commands
import cgi,re,sys
print "Content-Type: text/html"
print

for i in sys.stdin:
	j=i.strip()
	if int(j[1]) == 1:
		print "jan"
	elif int(j[1]) == 2:
		print "feb"
	elif int(j[1]) == 3:
		print "mar"
	elif int(j[1]) == 4:
		print "apr"
	elif int(j[1]) == 5:
		print "may"
	elif int(j[1]) == 6:
		print "jun"
	elif int(j[1]) == 7:
		print "jul"
	elif int(j[1]) == 8:
		print "aug"
	elif int(j[1]) == 9:
		print "sept"
	elif int(j[1]) == 10:
		print "oct"
	elif int(j[1]) == 11:
		print "nov"
	elif int(j[1]) == 12:
		print "dec"




#!/usr/bin/python
import cgi
import os,commands

print "content-type: text/html"
 

menuch=cgi.FormContent()['setup'][0]
if menuch == "automatic":
	print "location: ../dockernamenode.html"
	print
elif menuch == "manual":
	print "location: ../namenode.html"
        print

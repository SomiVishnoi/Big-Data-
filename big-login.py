#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"
#print
#print "hi"
username=cgi.FormContent()['username'][0]
password=cgi.FormContent()['password'][0]
#print username
auser="bigdata"
apassword="redhat"

if username == auser and password == apassword:
#	print "user authenticated"
##	print "<a href='../form.html'>click here to app</a>"
	print "location: ../big-menu.html"
	print
else:
#	print "login incorrect" 
	print "location: ../big-login.html"	
	print

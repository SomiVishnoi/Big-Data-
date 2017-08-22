#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print
num=cgi.FormContent()['num'][0]
os.system("sudo chown apache /webcontent/scripts/count.txt")
fl=open('/webcontent/scripts/count.txt','w')
fl.write(num)
fl.close()

print "<form action='docker_shell2.py'>"
i=0
while i < int(num):
	print "enter name of container{0}<input type='text' name='ip_dn{0}' />".format(i)
	print "<br />"
	i = i+1
print "<input type='submit' />"
print "</form>"




#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print


#print "hello"
count=cgi.FormContent()['count'][0]
folder=cgi.FormContent()['folder'][0]
size=cgi.FormContent()['size'][0]
#count='1'
#folder='data'
#size='100'
#master_ip='192.156.23.11'

os.system("sudo chown apache /webcontent/scripts/count.txt")
fl=open('/webcontent/scripts/count.txt','w')
fl.write(count+ "\n")
fl.write(folder+ "\n")
fl.write(size)
fl.close()

print "<form action='datanode2.py'>"
i=0
while i < int(count):
	print "enter ip for datanode {0}<input type='text' name='ip_dn{0}' />".format(i)
	print "<br />"
	i = i+1
print "<input type='submit' />"
print "</form>"








#!/usr/bin/python2
import cgi
import commands,os

print "Content-Type: text/html"
#print
#print "hi"


#print
os.system("sudo chown apache /files/docker_ip.txt")
fi=open('/files/docker_ip.txt','r')
ip=fi.read()
fi.close()
ip.strip("\n")
name=cgi.FormContent()['x'][0]
a=commands.getstatusoutput("sshpass  -p redhat  ssh -o stricthostkeychecking=no root@{0} sudo docker start {1}".format(ip,name))
#print a
if a[0]==0:
	print "location: docker_new.py"
	print

else:
	print "error"


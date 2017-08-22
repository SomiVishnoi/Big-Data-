#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
#print
name=cgi.FormContent()['con'][0]
imgname=cgi.FormContent()['imgname'][0]
#print imgname
#name='aa'
#imgname='centos:latest'
os.system("sudo chown apache /files/docker_ip.txt")
fi=open('/files/docker_ip.txt','r')
ip=fi.read()
fi.close()
ip.strip("\n")
#print ip
#ip='192.168.43.40'
i=commands.getstatusoutput("sshpass  -p redhat  ssh -o stricthostkeychecking=no root@{0} docker inspect {1}".format(ip,name))
#print i

if i[0]==0:
	print "container already running"
	print "<a href='docker_new.html'>click here to go back<>"
else:
	a=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker run -dit --name {1} {2}".format(ip,name,imgname))
	print "location: ../docker_new.html"
	print







#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print
text=cgi.FormContent()['txtm'][0]
#print text
#os.system("sudo systemctl restart docker")
#os.system("sudo docker run -dit --name shell_online centos:latest")
commands.getoutput("sudo docker start shell_online")

os.system("sudo chown apache /files/text.txt")
f1=open('/files/text.txt','w')
f1.write(text)
f1.close()
#out=commands.getstatusoutput("sudo docker exec shell_online {0}".format(text))
#print out

f3=open('/files/text.txt','r')
for i in f3:
	print i + ":"
	out=commands.getstatusoutput("sudo docker exec shell_online {0}".format(i))
#	out=os.system("sudo docker exec shell_online {0}".format(i))	
	print out
	print "<br />"
f3.close()	

print "<br />"
print "<a href='../docker_new.html'>click here to go to menu</a>"


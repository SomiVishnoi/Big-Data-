#!/usr/bin/python2
import os
import commands
import cgi,re,sys
print "Content-Type: text/html"
print
fq=cgi.FormContent()['fileq'][0]
os.system("chown apache /files/hadoop-client.txt")
fe=open('/files/hadoop-client.txt','r')
ip=fe.read()
fe.close()
ip.strip('\n')
sc=commands.getstatusoutput("sshpass -p redhat scp -o stricthostkeychecking=no /webcontent/scripts/client_mnth_mapper.py root@{0}:/".format(ip))

sy=commands.getstatusoutput("sshpass -p redhat scp -o stricthostkeychecking=no /webcontent/scripts/client_mnth_reducer.py root@{0}:/".format(ip))


sq=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar --input {1} -mapper ./client_mnth_mapper.py -file /client_mnth_mapper.py -reducer ./client_mnth_reducer.py -file /client_mnth_reducer.py -output /out123.txt".format(ip,fq))

if sq[0] == 0:
	out=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} hadoop fs -cat /out123.txt/part-r-00000".format(ip))	
	print out[1]
	print "<a href='../clientfinal.html'>click here to go back</a>"
else:
	print "error"
	print "<a href='../clientfinal.html'>click here to go back</a>"

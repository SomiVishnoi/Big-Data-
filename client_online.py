#!/usr/bin/python2
import os
import commands
import cgi
print "Content-Type: text/html"
print
#data=os.environ['HTTP_COOKIE']
#master_ip=data.split("=")[1]
txtm=cgi.FormContent()['txtm'][0]
txtr=cgi.FormContent()['txtr'][0]
fileq=cgi.FormContent()['fileq'][0]
os.system("chown apache /webcontent/scripts/client_online_mapper.py")
fw=open('/webcontent/scripts/client_online_mapper.py','w')
fw.write(txtm)
fw.close()
os.system("chown apache /webcontent/scripts/client_online_reducer.py")
fw=open('/webcontent/scripts/client_online_reducer.py','w')
fw.write(txtr)
fw.close()
os.system("chown apache /files/hadoop-client.txt")
fe=open('/files/hadoop-client.txt','r')
ip=fe.read()
fe.close()
ip.strip('\n')
sc=commands.getstatusoutput("sshpass -p redhat scp -o stricthostkeychecking=no /webcontent/scripts/client_online_mapper.py root@{0}:/".format(ip))
sy=commands.getstatusoutput("sshpass -p redhat scp -o stricthostkeychecking=no /webcontent/scripts/client_online_reducer.py root@{0}:/".format(ip))
sq=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar --input {1} -mapper ./client_online_mapper.py -file /client_online_mapper.py -reducer ./client_online_reducer.py -file /client_online_reducer.py -output /out123.txt".format(ip,fq))
if sq[0] == 0:
	out=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} hadoop fs -cat /out123.txt/part-r-00000".format(ip))	
	print out[1]
	print "<a href='../clientfinal.html'>click here to go back</a>"
else:
	print "error"
	print "<a href='../clientfinal.html'>click here to go back</a>"





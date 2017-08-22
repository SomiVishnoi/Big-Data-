#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
#print


os.system("sudo chown apache /files/jobtracker_ip.txt")
f1=open('/files/jobtracker_ip.txt','r')
jobtracker_ip=f1.read()
f1.close()
k=0
ulist=[]
var=[]
os.system("sudo chown apache /webcontent/scripts/taskcount.txt")
fl=open('/webcontent/scripts/taskcount.txt','r')
for i in fl:
	var.append(i.rstrip('\n'))
count=var[0]
#folder=var[1]
#size=var[2]
while k < int(count):
	ip=cgi.FormContent()['ip_tt{0}'.format(k)][0]
	ulist.append(ip)
	k = k + 1
mapred='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n'.format(jobtracker_ip)
os.system("sudo chown apache /files/TT.txt")
f1=open('/files/TT.txt','w')
f1.write(mapred + '\n')
f1.close()

#print "written"
task="""---
- hosts: [TT]
  tasks:
    - copy: 
        src: "/files/TT.txt"
        dest: "/etc/hadoop/mapred-site.xml"
    - command: hadoop-daemon.sh start tasktracker"""


os.system("sudo chown apache /webcontent/scripts/tasktracker.yml")
fh=open('/webcontent/scripts/tasktracker.yml','w')
fh.write(task)
fh.close()

k=0
hostdata=""
while k < int(count):
	hostdata = hostdata + ulist[k] +" ansible_ssh_user=root ansible_ssh_pass=redhat\n"
	k = k + 1

#print hostdata
os.system("sudo chown apache /etc/ansible/hosts")

os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[TT]\n")
host.write(hostdata)
host.close()

os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook /webcontent/scripts/tasktracker.yml")
#print pr
if pr[0]==0:			
	print "location: ../success.html"
	print 
else:
	print "location: ../error.html"
	print 





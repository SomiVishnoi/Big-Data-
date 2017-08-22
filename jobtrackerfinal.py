#!/usr/bin/python2
import os
import commands
import cgi
print "Content-Type: text/html"
#print
#data=os.environ['HTTP_COOKIE']
#master_ip=data.split("=")[1]
os.system("sudo chown apache /files/namenode_ip.txt")
f1=open('/files/namenode_ip.txt','r')
master_ip=f1.read()
f1.close()
#master_ip='192.168.43.21'
ip=cgi.FormContent()['ip'][0]

mapred='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n'.format(ip)
os.system("sudo chown apache /files/JJ.txt")
f1=open("/files/JJ.txt","w")
f1.write(mapred + '\n')
f1.close()
#print "file mapred written"

core='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n'.format(master_ip)
os.system("sudo chown apache /files/JJcore.txt")
f1=open('/files/JJcore.txt','w')
f1.write(core + '\n')
f1.close()
#print "file core written"

#namenode.yml
job="""---
- hosts: jobtracker
  tasks:
    - copy:
        src: "/files/JJcore.txt"
        dest: "/etc/hadoop/core-site.xml"
    - copy:
        src: "/files/JJ.txt"
        dest: "/etc/hadoop/mapred-site.xml" 
    - command: hadoop-daemon.sh start jobtracker"""

os.system("sudo chown apache /webcontent/scripts/jobtracker.yml")
fh=open('/webcontent/scripts/jobtracker.yml','w')
fh.write(job)
fh.close()
 
#print "file written"

os.system("sudo chown apache /etc/ansible/hosts")


os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[jobtracker]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ip))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/jobtracker.yml")
#print pr
os.system("sudo chown apache /files/jobtracker_ip.txt")
f1=open('/files/jobtracker_ip.txt','w')
f1.write(ip)
f1.close()
#print "yml run"

#if pr[0]==0:
print "location: ../tasktracker.html"
print 
#else:
#	print "location: ../error.html"
#	print "error" 






#!/usr/bin/python2
import os
import commands
import cgi
print "Content-Type: text/html"
#print

ip=cgi.FormContent()['ip'][0]
folder=cgi.FormContent()['folder'][0]
#print ip

hdfs='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{0}</value>\n</property>\n</configuration>\n'.format(folder)
os.system("sudo chown apache /files/name-hdfs-site.txt")
f1=open("/files/name-hdfs-site.txt","w")
f1.write(hdfs + '\n')
f1.close()
#print "file hdfs written"

core='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n'.format(ip)
os.system("sudo chown apache /files/name-core-site.txt")
f1=open('/files/name-core-site.txt','w')
f1.write(core + '\n')
f1.close()
#print "file core written"

#namenode.yml
name="""---
- hosts: namenode
  tasks:
    - copy:
        src: "/files/name-core-site.txt"
        dest: "/etc/hadoop/core-site.xml"
    - copy:
        src: "/files/name-hdfs-site.txt"
        dest: "/etc/hadoop/hdfs-site.xml"
   
    - command: hadoop namenode -format 
    - command: hadoop-daemon.sh start namenode"""

os.system("sudo chown apache /webcontent/scripts/namenode.yml")
fh=open('/webcontent/scripts/namenode.yml','w')
fh.write(name)
fh.close()
 
#print "file written"

os.system("sudo chown apache /etc/ansible/hosts")


os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[namenode]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ip))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/namenode.yml")
#print pr
os.system("sudo chown apache /files/namenode_ip.txt")
f1=open('/files/namenode_ip.txt','w')
f1.write(ip)
f1.close()

if pr[0]==0:
#	va=commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} cat /{1}/current/VERSION | grep "namespaceID"'.format(ip,folder))
#	version=va[1].split("=")[1]
#	print "set-cookie: ip_namenode={0}".format(ip)
#	print "set-cookie: version={0}".format(version)
	print "location: ../datanode.html"
	print
else:
	print "location: ../error.html"
	print 






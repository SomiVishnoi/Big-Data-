#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print

#data=os.environ['HTTP_COOKIE']
#master_ip=data.split("=")[1]
#ver_ip=data.split('=')[1]
#master_ip=ver_ip.split(";")[0]
#version=ver_ip.split(";")[1]
os.system("sudo chown apache /files/namenode_ip.txt")
f1=open('/files/namenode_ip.txt','r')
master_ip=f1.read()
f1.close()
#master_ip='192.168.43.21'
#print "ip"
k=0
ulist=[]
var=[]
os.system("sudo chown apache /webcontent/scripts/count.txt")
fl=open('/webcontent/scripts/count.txt','r')
for i in fl:
	var.append(i.rstrip('\n'))
count=var[0]
folder=var[1]
size=var[2]
while k < int(count):
	ip=cgi.FormContent()['ip_dn{0}'.format(k)][0]
	ulist.append(ip)
	k = k + 1

	
hdfs='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/media/{0}</value>\n</property>\n</configuration>\n'.format(folder)
os.system("sudo chown apache /files/data-hdfs-site.txt")
f1=open("/files/data-hdfs-site.txt","w")
f1.write(hdfs + '\n')
f1.close()

core='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n'.format(master_ip)
os.system("sudo chown apache /files/data-core-site.txt")
f1=open('/files/data-core-site.txt','w')
f1.write(core + '\n')
f1.close()

#print "written"
name="""---
- hosts: datanode
  tasks:
        - lvol:
           vg: "storage"
           lv: "{0}"
           size: "{1}"
        - filesystem: 
           fstype: ext4
           dev: "/dev/storage/{0}"
        - file:
           state: directory
           path: "/media/{0}"

        - mount:
           path: "/media/{0}"
           src: "/dev/storage/{0}"
           fstype: ext4
           state: present

        - copy:
           src: "/files/data-core-site.txt"
           dest: "/etc/hadoop/core-site.xml"

        - copy:
           src: "/files/data-hdfs-site.txt"
           dest: "/etc/hadoop/hdfs-site.xml"
        - command : hadoop-daemon.sh start datanode""".format(folder,size)


os.system("sudo chown apache /webcontent/scripts/datanode.yml")
fh=open('/webcontent/scripts/datanode.yml','w')
fh.write(name)
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
host.write("[datanode]\n")
host.write(hostdata)
host.close()

os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook /webcontent/scripts/datanode.yml")
#print pr
if pr[0]==0:
#	k=0
#	while k < int(count): 
#		va=commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} cat /media/{1}/current/VERSION | grep "namespaceID"'.format(ip,folder))
#		version_d=va[1].split("=")[1]
#		if version_d==version:
#			pass
#		else:
#			print "location: ../error.html"
#			print
#						
#	print "location: ../success.html"
	print "success"
	print "<a href='../big-menu.html'>click here to go back to menu</a>"
else:
#	print "location: ../error.html"
	print "error"
	print "<a href='../big-menu.html'>click here to go back to menu</a>"





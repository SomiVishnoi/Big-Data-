#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print


print "hello"
master_ip='192.168.43.21'
num=cgi.FormContent()['num'][0]
print num 


doc="""---
- hosts: jt
  tasks:
  - service:
         name: "docker"
         state: started
  - command: docker run -dit --name mapdoc1 doc_hadoop:v1""" 

os.system("sudo chown apache /webcontent/scripts/dock.yml")
fh=open('/webcontent/scripts/dock.yml','w')
fh.write(doc)
fh.close()

os.system("sudo chown apache /etc/ansible/hosts")

os.system("sudo chown apache /files/hosts_list.txt")
hostdoc=open('/files/hosts_list.txt','w')
hostdoc.write("[jt]\n192.168.43.33 ansible_ssh_user=root ansible_ssh_pass=redhat\n")
hostdoc.close()


os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")
pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/dock.yml")
print pr
print "jobtracker run"
"""
doc_ip=commands.getstatusoutput('sshpass -p redhat  ssh -o stricthostkeychecking=no root@192.168.43.33  docker inspect mapdoc1 | jq ".[].NetworkSettings.IPAddress"')
doc_jobtracker_ip=doc_ip[1]
print "ip get"
"""
doc_jobtracker_ip='172.17.0.2'
core='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>http://{0}:10001</value>\n</property>\n</configuration>\n'.format(master_ip)
os.system("sudo chown apache /files/jt-core-site.txt")
f1=open("/files/jt-core-site.txt","w")
f1.write(core + '\n')
f1.close()
print "file core written"

mapred='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>hdfs://{0}:9001</value>\n</property>\n</configuration>\n'.format(doc_jobtracker_ip)
os.system("sudo chown apache /files/mapred.txt")
f1=open('/files/mapred.txt','w')
f1.write(mapred + '\n')
f1.close()
print "file mapred written"


docn="""---
- hosts: jt
  tasks:
   - service: 
       name: "docker"
       state: started
   - command: docker start mapdoc1
   - copy:
       src: "/files/mapred.txt"
       dest: "/"
   - copy:
       src: "/files/jt-core-site.txt"
       dest: "/"
   - command: docker cp /mapred.txt mapdoc1:/etc/hadoop/mapred-site.xml
   - command: docker cp /jt-core-site.txt mapdoc1:/etc/hadoop/core-site.xml
   - command: docker exec mapdoc1 hadoop-daemon.sh start jobtracker
   - command: docker exec mapdoc1 /usr/java/jdk1.7.0_79/bin/jps
"""

os.system("sudo chown apache /webcontent/scripts/dock.yml")
fh=open('/webcontent/scripts/dock.yml','w')
fh.write(docn)
fh.close()

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/dock.yml")
print "set jt"

if pr[0]==0:
	i=0
	while i < int(num):
	
		mapred='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n'.format(doc_jobtracker_ip)
		os.system("sudo chown apache /files/mapred.txt")
		f1=open("/files/mapred.txt","w")
		f1.write(mapred + '\n')
		f1.close()
		print "file mapred written"
		Tasktracker= """---
                - hosts: jt
                  tasks:
                   - service:
                       name: "docker"
                       state: started
                   - command: docker run -dit --name doc_task{0} doc_hadoop:v1
                   - command: docker start doc_task{0}
                   - copy:   
                       src: "/files/mapred.txt"
                       dest: "/"
                   - command: docker cp /mapred.txt doc_task{0}:/etc/hadoop/mapred-site.xml
                   - command: docker exec doc_task{0} hadoop-daemon.sh start tasktracker""".format(i)


		os.system("sudo chown apache /webcontent/scripts/dock.yml")
		fh=open('/webcontent/scripts/dock.yml','w')
		fh.write(Tasktracker)
		fh.close()
		run=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/dock.yml")
		print run
		print "i run"
		i=i+1
	if run[0]==0:
		print "location: ../success.html"
#		print
#	else:
		print "location: ../error.html"
else:
#	print "location: ../error.html"
	print "error"



 


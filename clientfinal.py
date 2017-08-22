#!/usr/bin/python2
import os
import commands
import cgi
print "Content-Type: text/html"
print
#data=os.environ['HTTP_COOKIE']
#master_ip=data.split("=")[1]

os.system("sudo chown apache /files/master_ip.txt")
fw=open('/files/master_ip.txt','r')
master_ip=fw.read()
fw.close()
ip=cgi.FormContent()['ip'][0]
choice=cgi.FormContent()['objst'][0]
#print choice
os.system("sudo chown apache /files/jobtracker_ip.txt")
f1=open('/files/jobtracker_ip.txt','r')
jobtracker_ip=f1.read()
jobtracker_ip.strip('\n')
f1.close()
os.system("sudo chown apache /files/hadoop-client.txt")
fe=open('/files/hadoop-client.txt','w')
fe.write(ip)
fe.close()
if choice == 'upload':
	mapred='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n'.format(jobtracker_ip)
	os.system("sudo chown apache /files/mapred.txt")
	f1=open("/files/mapred.txt","w")
	f1.write(mapred + '\n')
	f1.close()
#	print "file mapred written"

	core='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n'.format(master_ip)
	os.system("sudo chown apache /files/jt-core-site.txt")
	f1=open('/files/jt-core-site.txt','w')
	f1.write(core + '\n')
	f1.close()
#	print "file core written"

	#namenode.yml
	client="""---
        - hosts: client
          tasks:
             - copy:
                src: "/files/mapred.txt"
                dest: "/etc/hadoop/mapred-site.xml
             - copy:
                src: "/files/jt-core-site.txt"
                dest: "/etc/hadoop/core-site.xml" """
	os.system("sudo chown apache /webcontent/scripts/client.yml")
	fh=open('/webcontent/scripts/client.yml','w')
	fh.write(client)
	fh.close()
	 
#	print "aa file written"

	os.system("sudo chown apache /etc/ansible/hosts")


	os.system("sudo chown apache /files/hosts_list.txt")
	host=open('/files/hosts_list.txt','w')
	host.write("[client]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ip))
	host.close()
																																																																																																																																																																																																																											
	os.system("sudo chown apache /files/aa.txt")
	os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
	os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

	pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/client.yml")
	print "client set"
	print "<form action='/scripts/client_upload.py' >"
	print "Enter path of file:<input type='text' name='fileq' />"
	print "<input type='submit' />"
	print "</form>"
	print "<a href='../clientfinal.html'>click here to go to menu</a>"
elif choice=='wordc':
	print "<form action='/scripts/client_mnth.py' >"
	print "Enter file name<input type='text' name='fileq' />"
	print "<input type='submit' />"
	print "</form>"
	print "<a href='../clientfinal.html'>click here to go to menu</a>"
elif choice == 'sort':
	print "<form action='/scripts/client_city.py' >"
	print "Enter file name <input type='text' name='fileq' />"
	print "<input type='submit' />"
	print "</form>"
	print "<a href='../clientfinal.html'>click here to go to menu</a>"
elif choice == 'num':
	print "<form action='/scripts/client_dist.py' >"
	print "Enter <input type='text' name='fileq' />"
	print "<input type='submit' />"
	print "</form>"
	print "<a href='../clientfinal.html'>click here to go to menu</a>"
elif choice == 'online':
	print "<h1>Online portal</h1>"
	print "<form action='/scripts/client_online.py' >"
	print "Enter <input type='text' name='fileq' />"
	print "<h1>Mapper code</h1>"
	print "<textarea cols='100' rows='50' name='txtm'></textarea>"
	print "<h1>Reducer code</h1>"
	print "<textarea cols='100' rows='50' name='txtr'></textarea>"
	print "<input type='submit' />"
	print "</form>"
	print "<a href='../clientfinal.html'>click here to go to menu</a>"










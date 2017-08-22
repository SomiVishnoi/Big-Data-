#!/usr/bin/python
import cgi
import os,commands

print "content-type: text/html"
menuch=cgi.FormContent()['setup'][0]
if menuch == "hdfs-cluster":
	print "location: ../hdfs.html"
	print
elif menuch == "mapreduce-cluster":
	print "location: ../mapr.html"
        print
elif menuch == "client":
	print "location: ../clientfinal.html"
        print
elif menuch == "docker":
	print "location: ../docker_new.html"
        print
elif menuch == "hadoop2":
	print "location: ../ver2.html"
        print

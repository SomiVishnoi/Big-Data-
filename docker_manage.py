#!/usr/bin/python2


import commands

print "content-type: text/html"
print

print """
<script>
function start(mycname)
{
//alert('hello');

document.location='docker-start.py?x=' + mycname;
}
function stop(mycname)
{
//alert('hello');

document.location='docker-stop-.py?x=' + mycname;
}
function remove(mycname)
{
//alert('hello');

document.location='docker-remove.py?x=' + mycname;
}
</script>
"""

#os.system("sudo chown apache /files/docker_ip.txt")
#os.system("sudo chown apache  /usr/share/httpd")
fi=open('/files/docker_ip.txt','r')
ip=fi.read()
fi.close()
print "<table border='5'>"
print "<tr><th>Image Name</th><th>ContainerName</th><th>Status</th><th>Stop</th><th>Start</th><th>Remove</th></tr>"

z=1
for i in commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} sudo docker ps -a".format(ip)).split('\n'):
	if z == 1:
		z+=1
		pass
	else:
		j=i.split()
		cStatus=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1],ip))
		
		print "<tr><td>" + j[1] + "</td><td>" + j[-1] + "</td><td>" + cStatus[-1] +  "</td><td>   <input value='" + j[-1]    +  "' type='button' onclick=stop(this.value)  />  </td><td>     <input value='" + j[-1]    +  "' type='button' onclick=start(this.value)  /></td><td>  <input value='" + j[-1]    +  "' type='button' onclick=remove(this.value)  /> </td></tr>"

print "</table>"












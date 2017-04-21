import sys
from termcolor import colored
from subprocess import call
import os
import subprocess

alive_hosts = []
host_file = open("alive_hosts.txt","w")


def fping():
	p = subprocess.Popen(["fping","-g","192.168.1.0/24"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:
		if 'alive' in line:
			s = line.split(" ")
			alive_hosts.append(s[0])
			host_file.write(s[0]+"\n")
			print colored(line,'green')
		#else:
			#print colored(line,'red')

fping()
host_file.close()

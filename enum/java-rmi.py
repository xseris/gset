import sys
from termcolor import colored
from subprocess import call
import os
import subprocess


def test(host,port):
	p = subprocess.Popen(["nmap","--script","rmi-vuln-classloader","-p",port,host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')

print "Testing for RMI vulns:"
test(sys.argv[1],sys.argv[2])


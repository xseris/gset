import sys
from termcolor import colored
from subprocess import call
import os
import subprocess


def test(host):
	p = subprocess.Popen(["nbtscan","-v",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '<' in line:
			print colored(line,'green')

print "Scanning NetBIOS Name Table:"
test(sys.argv[1])

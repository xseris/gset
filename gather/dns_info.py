import sys
from termcolor import colored
from subprocess import call
import os
import subprocess

def mx_info(host):
	p = subprocess.Popen(["nslookup","-query=mx","host"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:
		print line

def ns_info(host):
	p = subprocess.Popen(["nslookup","-query=ns","host"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:
		print line

def dns_info(host):
	p = subprocess.Popen(["nslookup","-query=dns","-debug","host"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:
		print line

mx_info(sys.argv[1])
ns_info(sys.argv[1])
dns_info(sys.argv[1])

import sys
from termcolor import colored
from subprocess import call
import os
import subprocess


def test(host):
	p = subprocess.Popen(["nmap","--script","smb-enum-shares.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')
def test2(host):
	p = subprocess.Popen(["nmap","--script","smb-enum-names.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')
def test3(host):
	p = subprocess.Popen(["nmap","--script","smb-os-discovery.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')
def test4(host):
	p = subprocess.Popen(["nmap","--script","smb-double-pulsar-backdoor","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')

def test5(host):
	p = subprocess.Popen(["nmap","--script","smb-enum-domains.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')

def test6(host):
	p = subprocess.Popen(["nmap","--script","smb-enum-processes.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')

def test7(host):
	p = subprocess.Popen(["nmap","--script","smb-enum-sessions.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')

def test8(host):
	p = subprocess.Popen(["nmap","--script","smb-system-info.nse","-p445",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if '|' in line:
			print colored(line,'green')

print "SMB enumeration:"
test(sys.argv[1])
test2(sys.argv[1])
test3(sys.argv[1])
test4(sys.argv[1])
test5(sys.argv[1])
test6(sys.argv[1])
test7(sys.argv[1])
test8(sys.argv[1])

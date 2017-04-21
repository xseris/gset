import sys
from termcolor import colored
from subprocess import call
import os
import subprocess

global alive_hosts
global open_ports
host_file = open("alive_hosts.txt","r")


def read_file():
	global alive_hosts
	text = host_file.read()
	host_file.close()
	alive_hosts = text.split("\n")

def test_hosts():
	for host in alive_hosts:
		if host != "":
			print "++++++++++ Testing :",host,"++++++++++"
			print colored("Testing TCP/SYN Scan:",'yellow')
			test_tcp_syn(host)
			print colored("Testing TCP Connect:",'yellow')
			test_tcp_connect(host)
			print colored("Testing NULL Scan:",'yellow')
			test_null(host)
			print colored("Testing FIN Scan:",'yellow')
			test_fin(host)
			print colored("Testing XMAS Scan:",'yellow')
			test_xmas(host)
			print colored("Testing UDP Scan:",'yellow')
			test_udp(host)
			print colored("Retrieving OS info:",'yellow')
			test_os(host)

def test_tcp_syn(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sS","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			print colored(line,'green')

def test_tcp_connect(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sC","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			print colored(line,'green')
	print open_ports

def test_null(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sN","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			print colored(line,'green')

def test_fin(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sF","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			print colored(line,'green')

def test_xmas(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sX","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			print colored(line,'green')

def test_udp(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sU","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			print colored(line,'green')

def test_os(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-O",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'OS' in line:
			print colored(line,'green')


read_file()
host_file.close()
test_hosts()


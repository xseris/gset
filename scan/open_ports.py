import sys
from termcolor import colored
from subprocess import call
import os
import subprocess
import MySQLdb

global alive_hosts
global open_ports
host_file = open("../generated/alive_hosts.txt","r")


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
			fields = line.split()
			compose_and_insert(fields)
			print colored(line,'green')

def test_tcp_connect(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sC","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			fields = line.split()
			compose_and_insert(fields)
			print colored(line,'green')

def test_null(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sN","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			fields = line.split()
			compose_and_insert(fields)
			print colored(line,'green')

def test_fin(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sF","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			fields = line.split()
			compose_and_insert(fields)
			print colored(line,'green')

def test_xmas(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sX","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			fields = line.split()
			compose_and_insert(fields)
			print colored(line,'green')

def test_udp(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-sU","-sV",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'open' in line:
			fields = line.split()
			compose_and_insert(fields)
			print colored(line,'green')

def test_os(host):
	p = subprocess.Popen(["nmap","-n","-Pn","-O",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:	
		if 'OS' in line:
			print colored(line,'green')

def create_table():
	db = MySQLdb.connect("localhost","root","gt5er57","penetration" )
	cursor = db.cursor()
	cursor.execute("DROP TABLE IF EXISTS OPENPORTS")

	sql = """CREATE TABLE OPENPORTS (
		 PORTNUMBER  INT NOT NULL,
		 PROTOCOL  CHAR(3),
		 PORTSERVICE  CHAR(45),
		 SERVICEVERSION CHAR(100))"""
	cursor.execute(sql)
	# disconnect from server
	db.close()

def insert_record(portnum,protocol,service,version):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration" )
	cursor = db.cursor()
	sql = "INSERT INTO OPENPORTS(PORTNUMBER,PROTOCOL,PORTSERVICE,SERVICEVERSION) VALUES ('"+str(portnum)+"','"+protocol+"','"+service+"','"+version+"')"
	cursor.execute(sql)
	db.commit()
	db.close()

def compose_and_insert(f):
	pnum = f[0].split('/')[0]
	prot = f[0].split('/')[1]
	serv = f[2]
	vers = ""
	for n in range(0,len(f)):
		if n > 2:
			vers = vers+f[n]
	insert_record(pnum,prot,serv,vers)


create_table()
read_file()
host_file.close()
test_hosts()


import sys
from termcolor import colored
from subprocess import call
import os
import subprocess
import MySQLdb

global alive_hosts
global open_ports
host_file = open("../generated/alive_hosts.txt","r")

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

def get_records():
	db = MySQLdb.connect("localhost","root","gt5er57","penetration" )
	cursor = db.cursor()
	sql = "SELECT DISTINCT * FROM OPENPORTS ORDER BY PORTNUMBER"
	cursor.execute(sql)
	
	for (portnum,protocol,service,version) in cursor:
	  	print portnum,'\t',protocol,'\t',service,'\t',version
	db.commit()
	db.close()

get_records()


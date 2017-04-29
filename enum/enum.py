import sys
from termcolor import colored
from subprocess import call
import os
import subprocess
import MySQLdb

global open_ports
global port_protocols
global port_services

def read_db():
	global open_ports
	global port_protocols
	global port_services
	open_ports = []
	port_protocols = []
	port_services = []
	db = MySQLdb.connect("localhost","root","gt5er57","penetration" )
	cursor = db.cursor()
	sql = "SELECT DISTINCT * FROM OPENPORTS GROUP BY PORTNUMBER"
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		open_ports.append(row[0])
		port_protocols.append(row[1])
		port_services.append(row[2])
	db.close()

def enum():
	for service in port_services:
		if "netbios-ssn" in service:
			p = subprocess.Popen(["python","tcp445.py","192.168.1.3"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			out, err = p.communicate()
			outt = out.split("\n")
			for line in outt:	
				print colored(line,'green')


read_db()
enum()

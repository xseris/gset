import sys
from termcolor import colored
from subprocess import call
import os
import subprocess
import MySQLdb

def read_records(tablename,version):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration")
	cursor = db.cursor()
	sql = "SELECT * FROM "+tablename+" WHERE VERSION = '"+version+"'"
	cursor.execute(sql)
	for (ver,cve,score,typ,info) in cursor:
	  	print ver,'\t',cve,'\t',score,'\t',typ
	db.commit()
	db.close()

def read_records2(tablename):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration")
	cursor = db.cursor()
	sql = "SELECT * FROM "+tablename+" ORDER BY VERSION"
	cursor.execute(sql)
	for (ver,cve,score,typ,info) in cursor:
	  	print ver,'\t',cve,'\t',score,'\t',typ
	db.commit()
	db.close()

def read_records_verbose(tablename,version):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration")
	cursor = db.cursor()
	sql = "SELECT * FROM "+tablename+" WHERE VERSION = '"+version+"'"
	cursor.execute(sql)
	for (ver,cve,score,typ,info) in cursor:
	  	print ver,'\t',cve,'\t',score,'\t',typ,'\t',info
	db.commit()
	db.close()

def read_records2_verbose(tablename):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration")
	cursor = db.cursor()
	sql = "SELECT * FROM "+tablename+" ORDER BY VERSION"
	cursor.execute(sql)
	for (ver,cve,score,typ,info) in cursor:
	  	print ver,'\t',cve,'\t',score,'\t',typ,'\t',info
	db.commit()
	db.close()

if len(sys.argv)<3:
	read_records2(sys.argv[1])
elif len(sys.argv)==3:
	if '-v' in sys.argv[1]:
		read_records2_verbose(sys.argv[2])
	else:
		read_records(sys.argv[1],sys.argv[2])
else:
	read_records_verbose(sys.argv[2],sys.argv[3])

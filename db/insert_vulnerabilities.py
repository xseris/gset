import sys
from termcolor import colored
from subprocess import call
import os
import subprocess
import MySQLdb

host_file = open("to_insert.txt","r")

def create_table(tablename):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration")
	cursor = db.cursor()

	sql = """CREATE TABLE IF NOT EXISTS """+tablename+""" (
		 VERSION  CHAR(45),
		 CVE  CHAR(15),
		 SCORE  CHAR(4),
		 TYPE CHAR(20),
		 INFO TEXT)"""
	cursor.execute(sql)
	# disconnect from server
	db.close()

def compose_and_insert(tablename,version):
	text = host_file.read()
	lines = text.split('\n')
	for line in lines:
		parts = line.split('\t')
		print parts
		if line != '':
			insert_record(tablename,version,parts[0],parts[2],parts[1],parts[3])

def insert_record(tablename,version,cve,score,typ,info):
	db = MySQLdb.connect("localhost","root","gt5er57","penetration")
	cursor = db.cursor()
	sql = "INSERT INTO "+tablename+"(VERSION,CVE,SCORE,TYPE,INFO) VALUES ('"+version+"','"+cve+"','"+score+"','"+typ+"','"+info+"')"
	cursor.execute(sql)
	db.commit()
	db.close()


create_table(sys.argv[1])
compose_and_insert(sys.argv[1],sys.argv[2])

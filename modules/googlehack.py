#!/usr/bin/python
# Filename: googlehack.py

from google import search
import sys
from termcolor import colored
from subprocess import call
import os
import subprocess


def get_files(domain,typ):
	print "+++++ Checking for",typ,": +++++"
	for url in search('site:'+domain+' filetype:'+typ, stop=200):
		print "downloading",url
		print url.split('/')[-1]
		p = subprocess.Popen(["curl",url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p.communicate()
		out_file = open(url.split('/')[-1],"w")
		out_file.write(out)
		out_file.close()

def get_subdomains(domain):
	print "+++++ Checking for subdomains: +++++"
	subdomains = []
	for url in search('site:'+domain, stop=200):
		dom = url.split('/')[2]
		if not dom in subdomains:
			subdomains.append(dom)
			print colored(dom,'green')

version = '0.1'

# End of mymodule.py

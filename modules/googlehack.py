#!/usr/bin/python
# Filename: googlehack.py

from google import search
import sys
from termcolor import colored
from subprocess import call
import os
import subprocess


def get_files(domain,typ):
	print("+++++ Checking for",typ,": +++++")
	for url in search('site:'+domain+' filetype:'+typ, stop=200):
		print("downloading",url)
		print(url.split('/')[-1])
		p = subprocess.Popen(["curl",url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p.communicate()
		out_file = open(url.split('/')[-1],"wt")
		out_file.write(str(out))
		out_file.close()

def get_files_gui(domain,typ):
	files = []
	for url in search('site:'+domain+' filetype:'+typ, stop=200):
		files.append(url)
	return files

def get_subdomains(domain):
	print("+++++ Checking for subdomains: +++++")
	subdomains = []
	for url in search('site:'+domain, stop=200):
		dom = url.split('/')[2]
		if not dom in subdomains:
			subdomains.append(dom)
			print(colored(dom,'green'))

def get_subdomains_gui(domain):
	subdomains = []
	for url in search('site:'+domain, stop=200):
		dom = url.split('/')[2]
		if not dom in subdomains:
			subdomains.append(dom)
	return subdomains

version = '0.1'
descriptionfiles = 'search for files with a specific extension on given domain'
descriptionsubdomains = 'search for subdomains of given domain'

# End of mymodule.py

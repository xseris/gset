from google import search
import sys
from termcolor import colored
from subprocess import call
import os
import subprocess

global subdomains

def get_pdfs(domain):
	print "+++++ Checking for pdfs: +++++"
	for url in search('site:'+domain+' filetype:pdf', stop=20):
		print "downloading",url
		print url.split('/')[-1]
		p = subprocess.Popen(["curl",url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p.communicate()
		out_file = open(url.split('/')[-1],"w")
		out_file.write(out)
		out_file.close()

def get_subdomains(domain):
	print "+++++ Checking for subdomains: +++++"
	global subdomains
	subdomains = []
	for url in search('site:'+domain, stop=200):
		dom = url.split('/')[2]
		if not dom in subdomains:
			subdomains.append(dom)
			print colored(dom,'green')


get_pdfs(sys.argv[1])
get_subdomains(sys.argv[1])

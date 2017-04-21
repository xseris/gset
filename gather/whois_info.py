import sys
from termcolor import colored
from subprocess import call
import os
import subprocess

global registrant_organization
global registrant_address
global registrant_city
global registrant_CAP
global registrant_region
global registrant_nation

global admin_name
global admin_organization
global admin_address
global admin_city
global admin_CAP
global admin_region
global admin_nation

def whois(domain):
	p = subprocess.Popen(["whois",domain],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	i=0
	for line in outt:
		i=i+1
		if 'Registrant' in line:
			global registrant_organization
			global registrant_address
			global registrant_city
			global registrant_CAP
			global registrant_region
			global registrant_nation
			l = outt[i]
			registrant_organization=l.split(":")[1].lstrip()
			l = outt[i+1]
			registrant_address=l.split(":")[1].lstrip()
			l = outt[i+2]
			registrant_city=l.lstrip()
			l = outt[i+3]
			registrant_CAP=l.lstrip()
			l = outt[i+4]
			registrant_region=l.lstrip()
			l = outt[i+5]
			registrant_nation=l.lstrip()
		elif 'Admin' in line:
			global admin_name
			global admin_organization
			global admin_address
			global admin_city
			global admin_CAP
			global admin_region
			global admin_nation
			l = outt[i]
			admin_name = l.split(":")[1].lstrip()
			l = outt[i+1]
			admin_organization = l.split(":")[1].lstrip()
			l = outt[i+2]
			admin_address = l.split(":")[1].lstrip()
			l = outt[i+3]
			admin_city=l.lstrip()
			l = outt[i+4]
			admin_CAP=l.lstrip()
			l = outt[i+5]
			admin_region=l.lstrip()
			l = outt[i+6]
			admin_nation=l.lstrip()

whois(sys.argv[1])
print colored("Registrant:","green")
print registrant_organization
print registrant_address
print registrant_city
print registrant_CAP
print registrant_region
print registrant_nation
print colored("Admin:","green")
print admin_name
print admin_organization
print admin_address
print admin_city
print admin_CAP
print admin_region
print admin_nation

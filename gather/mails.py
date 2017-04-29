import sys
from termcolor import colored
from subprocess import call
import os
import subprocess

mails = []

def get_mails():
	p = subprocess.Popen(["python","../tools/theHarvester-master/theHarvester.py","-d","okkam.it","-l","300","-b","all"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:
		if '@' in line:
			mails.append(line)

get_mails()
print mails

#!/usr/bin/python
# Filename: mails.py

import os
import sys
from termcolor import colored
from subprocess import call
import subprocess
import argparse

def get_mails(domain):
	mails = []
	p = subprocess.Popen(["python","tools/theHarvester-master/theHarvester.py","-d",domain,"-l","300","-b","all"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	outt = out.split("\n")
	for line in outt:
		if '@' in line:
			mails.append(line)
	print(mails)

version = '0.1'
description = 'Gather all mails of the specified domain (@domain)'

# End of mymodule.py

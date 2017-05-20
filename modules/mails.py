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
	outt = out.split(bytes("\n", 'UTF-8'))
	for line in outt:
		if bytes('@', 'UTF-8') in line:
			mails.append((str)(line).replace("b'",""))
	return mails

version = '0.1'
description = 'Gather all mails of the specified domain (@domain)'

# End of mymodule.py

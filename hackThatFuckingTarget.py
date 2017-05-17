import os
import sys
from termcolor import colored
from subprocess import call
import subprocess
import argparse

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import mails
import dnsinfo
import googlehack


parser = argparse.ArgumentParser(description='A better description is required...')

#parser.add_argument('-d','--domain', metavar='N', type=int, nargs='+',
#                   help='an integer for the accumulator')

parser.add_argument('--mails', action='store_true', default=False,
                    dest='getmails',
                    help='Check mails on specified -d domain')

parser.add_argument('--dns', dest='dnsinfo', action='store', default='none',
                    help='Check dns reconds on specified -d domain')

parser.add_argument('--filetype', action='store', default='none',
                    dest='filetype',
                    help='Check for files of specified type in the specified -d domain')

parser.add_argument('-d', '--domain', dest='domain', action='store', default='none',
                    help='hack on specified domain')

args = parser.parse_args()

if 'none' not in args.domain:
	if args.getmails:
		print mails.get_mails(args.domain)
	if 'none' not in args.dnsinfo:
		if 'MX' in args.dnsinfo or 'mx' in args.dnsinfo:
			print dnsinfo.mx_info(args.domain)
		if 'DNS' in args.dnsinfo or 'dns' in args.dnsinfo:
			print dnsinfo.dns_info(args.domain)
		if 'NS' in args.dnsinfo or 'ns' in args.dnsinfo:
			print dnsinfo.ns_info(args.domain)
		else:
			print "Unknown record format. Please consider MX, NS or DNS."
	if 'none' not in args.filetype:
		print googlehack.get_files(args.domain,args.filetype)

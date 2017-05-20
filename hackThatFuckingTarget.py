import os
import sys
from termcolor import colored
from subprocess import call
import subprocess
import argparse
import locale

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from dialogpy import Dialog
import mails
import dnsinfo
import googlehack
import openports
import infogathermenu

tocompile = set()
compiled = set()
torun = set()
global domain
global filetype
global mail_list
global subdomain_list
global file_list

d = Dialog(dialog='dialog',autowidgetsize=True)

def midrun():
	d.gauge_start("Please wait...",1000,1000)
	step = (int)(100/len(torun))
	actual=0;
	text = ""
	for run in torun:
		if 'mail' in run:
			text = text+"[ Progress ]\t Checking for mails...\n"
			d.gauge_update(actual,text,True)
			global mail_list
			mail_list = mails.get_mails(domain)
			actual = actual+step
			text = text.replace("[ Progress ]", "[ Done ]")
			d.gauge_update(actual,text,True)
		if 'files' in run:
			text = text+"[ Progress ]\t Checking for files..\n"
			global file_list
			d.gauge_update(actual,text,True)
			file_list = googlehack.get_files_gui(domain,filetype)
			actual = actual+step
			text = text.replace("[ Progress ]", "[ Done ]")
			d.gauge_update(actual,text,True)
		if 'subdomain' in run:
			text = text+"[ Progress ]\t Checking for subdomains...\n"
			global subdomain_list
			d.gauge_update(actual,text,True)
			subdomain_list = googlehack.get_subdomains_gui(domain)
			actual = actual+step
			text = text.replace("[ Progress ]", "[ Done ]")
			d.gauge_update(actual,text,True)
	exit_code = d.gauge_stop()

def collect_missing():
	global domain
	global filetype
	for param in tocompile:
		code, string = d.inputbox("Almost done, just some few details: "+param,init="")
		if code == d.DIALOG_OK:	
			if 'domain' in param:
				domain = string
			if 'file' in param:
				filetype = string
	


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

parser.add_argument('--openports', action='store_true', default=False,
                    dest='scanport',
                    help='Check for openports on specified -d domain, with a specific scan')

parser.add_argument('--syn', action='store_true', default=False,
                    dest='scansyn',
                    help='Perform an SYN scan on the specified -d domain')

parser.add_argument('--tcp', action='store_true', default=False,
                    dest='scantcp',
                    help='Perform a TCP scan on the specified -d domain')

parser.add_argument('--null', action='store_true', default=False,
                    dest='scannull',
                    help='Perform a NULL scan on the specified -d domain')

parser.add_argument('--fin', action='store_true', default=False,
                    dest='scanfin',
                    help='Perform a FIN scan on the specified -d domain')

parser.add_argument('--xmas', action='store_true', default=False,
                    dest='scanxmas',
                    help='Perform a XMAS scan on the specified -d domain')

parser.add_argument('--udp', action='store_true', default=False,
                    dest='scanudp',
                    help='Perform an UDP scan on the specified -d domain')

parser.add_argument('--full', action='store_true', default=False,
                    dest='scanfull',
                    help='Perform a full scan on the specified -d domain')

parser.add_argument('--os', action='store_true', default=False,
                    dest='scanos',
                    help='Perform an OS scan on the specified -d domain')

parser.add_argument('--subdomains', action='store_true', default=False,
                    dest='subdomain',
                    help='Discover subdomains of specified -d domain')

parser.add_argument('-g', '--guided', action='store_true', default=False,
                    dest='guided',
                    help='Guided hack')

args = parser.parse_args()
	
if 'none' not in args.domain:
	if args.getmails:
		print(mails.get_mails(args.domain))
	if 'none' not in args.dnsinfo:
		if 'MX' in args.dnsinfo or 'mx' in args.dnsinfo:
			print(dnsinfo.mx_info(args.domain))
		if 'DNS' in args.dnsinfo or 'dns' in args.dnsinfo:
			print(dnsinfo.dns_info(args.domain))
		if 'NS' in args.dnsinfo or 'ns' in args.dnsinfo:
			print(dnsinfo.ns_info(args.domain))
		else:
			print("Unknown record format. Please consider MX, NS or DNS.")
	if 'none' not in args.filetype:
		print(googlehack.get_files(args.domain,args.filetype))
	if args.subdomain:
		print(googlehack.get_subdomains(args.domain))
	if args.scanport:
		if args.scansyn:
			print(openports.test_tcp_syn(args.domain))
		if args.scantcp:
			print(openports.test_tcp_connect(args.domain))
		if args.scannull:
			print(openports.test_null(args.domain))
		if args.scanfin:
			print(openports.test_fin(args.domain))
		if args.scanxmas:
			print(openports.test_xmas(args.domain))
		if args.scanudp:
			print(openports.test_udp(args.domain))
		if args.scanos:
			print(openports.test_os(args.domain))
		if args.scanfull:
			print(openports.test_full(args.domain))
else:
	if args.guided:
		locale.setlocale(locale.LC_ALL, '')
		if d.yesno("This is a stupid question, but, do you want to continue?") == d.DIALOG_OK:    		
			code, tags = d.checklist("Select all the phases you want to pass through:",
				choices=[("(0.0) Information Gathering", "", 0)],
				title="Check Penetration Testing",
				backtitle="A place to start ...")
			if code == d.DIALOG_OK:
				for tag in tags:
					if '0.0' in tag:
						code, tags = d.checklist("Select all modules to import:",
							choices = infogathermenu.get_data(),
							title="Module Selection",
							backtitle="Keep configuring ...")
						if code == d.DIALOG_OK:
							for tag in tags:
								if '0.0.1' in tag:
									tocompile.add("domain")
									torun.add("mail")
								if '0.0.2' in tag:
									tocompile.add("filetype")
									tocompile.add("domain")
									torun.add("files")
								if '0.0.3' in tag:
									tocompile.add("domain")
									torun.add("subdomain")
							collect_missing()
							midrun()
		else:
			code, tag = d.menu("OK, then you have two options:",
			choices=[("(1)", "Leave this fascinating example"),
			("(2)", "Leave this fascinating example")])

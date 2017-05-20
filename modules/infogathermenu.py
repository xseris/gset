import mails
import dnsinfo
import googlehack
import openports

def get_data():
	return [("(0.0.1) Mail Crawler", "version: "+mails.version+" -> "+mails.description , 0),
		("(0.0.2) File Crawler", "version: "+googlehack.version+" -> "+googlehack.descriptionfiles , 0),
		("(0.0.3) Subdomain Crawler", "version: "+googlehack.version+" -> "+googlehack.descriptionsubdomains , 0)]


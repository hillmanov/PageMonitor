import urllib2
import hashlib
import time
import gvoice
import ConfigParser
import smtplib
from email.mime.text import MIMEText

URL = ""
SMTP_SERVER = 'smtp.gmail.com:587'

# You need to create a base has to compare against. Use the instructions in the README to create this.
BASE_HASH = ''

INTERVAL = 10
# Comma separated list of phone numbers that you want notified
PHONE_NUMBERS = []
# Comma separated list of emails that you want notified
EMAIL_ADDRESSES = []

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

def is_same(content):
	return hashlib.sha224(content).hexdigest() == BASE_HASH
	
def send_message():
	username = config.get('Google', 'username')
	password = config.get('Google', 'password')
	
	gv_login = gvoice.GoogleVoiceLogin(username, password)
	text_sender = gvoice.TextSender(gv_login)
	text_sender.text = "Webpage has changed! {0}".format(URL)
	for phone_number in PHONE_NUMBERS:
		print "Sending text message to {0}".format(phone_number)
		text_sender.send_text(phone_number)
	
	server = smtplib.SMTP(SMTP_SERVER)
	server.starttls()
	server.login(username, password)
	for email_address in EMAIL_ADDRESSES:
		
		email_message = MIMEText(MESSAGE)
		email_message['From'] = '"WebMonitorBot" <{0}@gmail.com>'.format(username)
		email_message['Subject'] = 'Webpage has changed[{0}]!'.format(URL)
		email_message['To'] = email_address
		
		server.sendmail(email_message['From'], email_message['To'], email_message.as_string())
	server.quit()
	
while True:
	print "Checking {0} for changes...".format(URL)
	page_content = urllib2.urlopen.(URL).read()
	if not is_same(page_content):
		print "Change detected! Sending notification messages."
		send_message()
		break
	else:
		print "No change yet. Sleeping for {0} seconds".format(INTERVAL)
		time.sleep(INTERVAL)
	
	
	







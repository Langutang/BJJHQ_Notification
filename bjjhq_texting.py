
import smtplib
import sys
import webscrape as WS
 
CARRIERS = {
    "att": "@txt.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "johnvjlang@gmail.com"
PASSWORD = "ftwoplvboawibuty"

def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = '8123617413{}'.format(CARRIERS['att'])
	auth = (EMAIL, PASSWORD)

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP("smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail(auth[0], to_number, message)
 
 
if __name__ == "__main__":
	try:
		some_text = f'''\\
        {WS.message()}
        '''
		print(f"Sending this message: {some_text}")
		send(some_text)
	except smtplib.SMTPRecipientsRefused as e:
		print(e)
import os
import whitelist
import config

# Constants
text_from = whitelist.FROM
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Text recipients specified in textTo list
def text(bod, textTo):
	for recipient in textTo:
	    from twilio.rest import Client
	    client = Client(account_sid, auth_token)
	    message = client.messages.create(body=bod, from_=text_from, to=recipient)
	    print('Sent SMS to {}'.format(recipient))

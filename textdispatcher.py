import os
import whitelist

# Constants
text_from = whitelist.FROM
text_to = whitelist.NICK
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

def text(bod):
    from twilio.rest import Client
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=bod,
                         from_=text_from,
                         to=text_to,
                     )

    print('Sent SMS from {}'.format(message.sid))

#SDK Version: 6.17
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACdfef8c0c9b63a39ac98532fbc4391c45'
auth_token = '7cec45f55a690336dbd21f78eadbd699'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="I'm in.",
                     from_='+18084686236 ',
                     to='+18085896951'
                 )

print(message.sid)

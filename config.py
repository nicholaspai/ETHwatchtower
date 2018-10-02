import os

## read Heroku config vars
INFURA_API_KEY_MAIN = os.environ.get("INFURA_API_KEY_MAIN")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

## user wallets to monitor

# Owner of smart contracts
owner = os.environ.get("OWNER")
# Validator can set permissions on Regulator
validator = os.environ.get("VALIDATOR")

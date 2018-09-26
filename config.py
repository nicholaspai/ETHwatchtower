import os

# read Heroku config vars
INFURA_API_KEY_MAIN = os.environ.get("INFURA_API_KEY_MAIN")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# read global vars from .env
# INFURA_API_KEY_MAIN = os.getenv("INFURA_API_KEY_MAIN")
# TWILIO_SID = os.getenv("TWILIO_SID")
# TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


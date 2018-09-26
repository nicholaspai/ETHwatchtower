# setupWeb3: Export web3 object using infura to connect to mainnet
from web3 import Web3
import settings
import os

# Load constants from .env which are now present as system environment variable
INFURA_API_KEY_MAIN = os.getenv("INFURA_API_KEY_MAIN")

# Set provider using Infura node
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/" + INFURA_API_KEY_MAIN))

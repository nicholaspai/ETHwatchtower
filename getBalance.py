from setupWeb3 import w3
from textdispatcher import text

# Owner of smart contracts
owner = '0xB3801a04F1fc50B71d5c0776b0739add3AaDdc42'

# Validator can set permissions on Regulator
validator = '0xFE6EB9835041e16A67eeEEcdb7945aF27Bc5a28D'

# Minter can mint new CUSD
minter = validator

# Balances
ownerBalance = w3.eth.getBalance(owner)
validatorBalance = w3.eth.getBalance(validator)

# Balances using 18 decimals
ownerBalance_eth = w3.fromWei(ownerBalance, 'ether')
validatorBalance_eth = w3.fromWei(validatorBalance, 'ether')

# Get latest block
latestBlock = w3.eth.blockNumber

def textBalanceOwner():
	text(str("Owner has {} ETH".format(ownerBalance_eth)))

def textBalanceValidatorMinter():
	text(str("Minter&Validator has {} ETH".format(validatorBalance_eth)))

def textBlockNumber():
	text(str('Latest block number: {}'.format(latestBlock)))

def main():
	textBalanceOwner()
	textBalanceValidatorMinter()
	textBlockNumber()

main()

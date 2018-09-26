from setupWeb3 import w3
from textdispatcher import text
import time

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

def textBalance():
	latestBlock = w3.eth.blockNumber
	ownerBalance = str("Owner has {} ETH\n".format(ownerBalance_eth))
	validatorAndMinterBalance = str("Minter&Validator has {} ETH\n".format(validatorBalance_eth))
	blockNumber = str('Block number: {}\n'.format(latestBlock))
	text(ownerBalance + validatorAndMinterBalance + blockNumber)

def loop_main(poll_interval):
	while True:
		textBalance()
		time.sleep(poll_interval)

def main():
	loop_main(2)

main()

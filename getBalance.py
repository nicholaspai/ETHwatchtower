from setupWeb3 import w3
from textdispatcher import text
import time

# Owner of smart contracts
owner = '0xB3801a04F1fc50B71d5c0776b0739add3AaDdc42'

# Validator can set permissions on Regulator
validator = '0xFE6EB9835041e16A67eeEEcdb7945aF27Bc5a28D'

# Minter can mint new CUSD
minter = validator

# Return 1 if balance has increased, -1 if decreased, 0 if unchanged
def getBalance(address):
	latestBlock = w3.eth.blockNumber
	oldBalance = w3.fromWei(w3.eth.getBalance(address, block_identifier=latestBlock-1), 'ether')
	newBalance = w3.fromWei(w3.eth.getBalance(address), 'ether')
	if newBalance < oldBalance:
		result = ({'delta':-1, 'new': newBalance, 'old': oldBalance})
		return result
	elif newBalance > oldBalance:
		result = ({'delta': 1, 'new': newBalance, 'old': oldBalance})
		return result
	else:
		result = ({'delta': 0, 'new': newBalance, 'old': oldBalance})
		return result

def textBalanceOwner():
	deltaBalance = getBalance(owner)
	latestBlock = w3.eth.blockNumber
	blockNumber = str('Block number: {}\n'.format(latestBlock))
	if deltaBalance['delta'] == 1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Owner ETH balance increased\n' + ownerBalance + blockNumber)
	elif deltaBalance['delta'] == -1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Owner ETH balance decreased\n' + ownerBalance + blockNumber)
	else:
		print('Owner ETH balance unchanged' + blockNumber)

def textBalanceValidator():
	deltaBalance = getBalance(validator)
	latestBlock = w3.eth.blockNumber
	blockNumber = str('Block number: {}\n'.format(latestBlock))
	if deltaBalance['delta'] == 1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Validator&Minter ETH balance increased\n' + ownerBalance + blockNumber)
	elif deltaBalance['delta'] == -1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Validator&Minter ETH balance decreased\n' + ownerBalance + blockNumber)
	else:
		print('Validator&Minter ETH balance unchanged' + blockNumber)

def loop_main(poll_interval):
	while True:
		textBalanceOwner()
		textBalanceValidator()
		time.sleep(poll_interval)

def main():
	loop_main(2)

main()

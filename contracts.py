from setupWeb3 import w3
import json

##### Logic, 'model', contracts  ######

# Logic CUSD contract
with open('./contracts/CarbonDollar.json', 'r') as cusd_abi_definition:
	cusd_abi = json.load(cusd_abi_definition)['abi']
cusd_address = w3.toChecksumAddress('0x5369808868556d476d0ebbea81ead08cf1c73243')
cusd = w3.eth.contract(cusd_address, abi=cusd_abi)

# Logic WT0 contract
with open('./contracts/WhitelistedToken.json', 'r') as wt0_abi_definition:
	wt0_abi = json.load(wt0_abi_definition)['abi']
wt0_address = w3.toChecksumAddress('0xe481e0f7a66691e47e8b7c40953cd5dcc6fc2be3')
wt0 = w3.eth.contract(wt0_address, abi=wt0_abi)

# Logic WT0 Regulator contract
with open('./contracts/WTRegulator.json', 'r') as wt0_reg_abi_definition:
	wt0_reg_abi = json.load(wt0_reg_abi_definition)['abi']
wt0_reg_address = w3.toChecksumAddress('0xdd1fff57debf3131e021091be08aac62ccf0b61e')
wt0_reg = w3.eth.contract(wt0_reg_address, abi=wt0_reg_abi)

# Logic CUSD Regulator contract
with open('./contracts/CDRegulator.json', 'r') as cusd_reg_abi_definition:
	cusd_reg_abi = json.load(cusd_reg_abi_definition)['abi']
cusd_reg_address = w3.toChecksumAddress('0x3b4c4deabe37606de5be72d040c19a2f6ae34d96')
cusd_reg = w3.eth.contract(cusd_reg_address, abi=cusd_reg_abi)

##### Active contracts #####

# CUSD Factory contract
with open('./contracts/CDFactory.json', 'r') as cusd_factory_abi_definition:
	cusd_factory_abi = json.load(cusd_factory_abi_definition)['abi']
cusd_factory_address = w3.toChecksumAddress('0x47386efa5d4887aef97a73d5d14905d005200072')
cusd_factory = w3.eth.contract(cusd_factory_address, abi=cusd_factory_abi)

# Active CUSD contract
cusd_active_address = cusd_factory.functions.getToken(0).call()
cusd_active = w3.eth.contract(cusd_active_address, abi=cusd_abi)

# WT0 Factory contract
with open('./contracts/WTFactory.json', 'r') as wt0_factory_abi_definition:
	wt0_factory_abi = json.load(wt0_factory_abi_definition)['abi']
wt0_factory_address = w3.toChecksumAddress('0xe92eab07e1491824cab0628099c81a8a7b190ffd')
wt0_factory = w3.eth.contract(wt0_factory_address, abi=wt0_factory_abi)

# Active WT0 contract
wt0_active_address = wt0_factory.functions.getToken(0).call()
wt0_active = w3.eth.contract(wt0_active_address, abi=wt0_abi)

# Regulator Factory contract
with open('./contracts/RegulatorFactory.json', 'r') as reg_factory_abi_definition:
	reg_factory_abi = json.load(reg_factory_abi_definition)['abi']
reg_factory_address = w3.toChecksumAddress('0xe7c888d9f5eed1be9eeb4a2ddebe437b0ac5e63e')
reg_factory = w3.eth.contract(reg_factory_address, abi=reg_factory_abi)

# Active WT0 Regulator contract
wt0_reg_active_address = reg_factory.functions.getRegulatorProxy(1).call()
wt0_reg_active = w3.eth.contract(wt0_reg_active_address, abi=wt0_reg_abi)

# Active CUSD Regulator contract
cusd_reg_active_address = reg_factory.functions.getRegulatorProxy(0).call()
cusd_reg_active = w3.eth.contract(cusd_reg_active_address, abi=cusd_reg_abi)



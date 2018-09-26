from contracts import (
	cusd_active,
	cusd_factory,
	wt0_active,
	wt0_factory,
	reg_factory,
	cusd_reg_active,
	wt0_reg_active
)

def getAddresses():
	print('CUSD: {}'.format(cusd_active.address))
	print('CUSD factory: {}'.format(cusd_factory.address))
	print('WT0: {}'.format(wt0_active.address))
	print('WT0 factory: {}'.format(wt0_factory.address))
	print('Regulator factory: {}'.format(reg_factory.address))
	print('CUSD regulator: {}'.format(cusd_reg_active.address))
	print('WT0 regulator: {}'.format(wt0_reg_active.address))

# def getEvents(contract):

def main():
	getAddresses()

main()

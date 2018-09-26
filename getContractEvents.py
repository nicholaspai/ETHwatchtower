from setupWeb3 import w3
from contracts import (
	cusd_active,
	cusd_factory,
	wt0_active,
	wt0_factory,
	reg_factory,
	cusd_reg_active,
	wt0_reg_active
)
import time

def getAddresses():
	print('CUSD: {}'.format(cusd_active.address))
	print('CUSD factory: {}'.format(cusd_factory.address))
	print('WT0: {}'.format(wt0_active.address))
	print('WT0 factory: {}'.format(wt0_factory.address))
	print('Regulator factory: {}'.format(reg_factory.address))
	print('CUSD regulator: {}'.format(cusd_reg_active.address))
	print('WT0 regulator: {}'.format(wt0_reg_active.address))

def handle_event(event):
	print(event)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

def main():
	# not working for now: createFilter() not allowed through an Infura node
	# event_filter = cusd_reg_active.events.LogWhitelistedUser.createFilter(fromBlock="latest")
	# log_loop(event_filter, 2)

main()

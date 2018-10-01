from getBalance import textBalanceOwner, textBalanceValidator
import whitelist
import time
import os

def loop_main(poll_interval):
	# Who will receive the alerts
	recipients = [whitelist.NICK]
	print('INFURA key: {}'.format(os.environ.get("INFURA_API_KEY_MAIN")))
	while True:
		textBalanceOwner(recipients)
		textBalanceValidator(recipients)
		time.sleep(poll_interval)

def main():
	loop_main(2)

main()
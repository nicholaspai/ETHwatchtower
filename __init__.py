from getBalance import textBalanceOwner, textBalanceValidator
import whitelist
import time

def loop_main(poll_interval):
	# Who will receive the alerts
	recipients = [whitelist.NICK]
	while True:
		textBalanceOwner(recipients)
		textBalanceValidator(recipients)
		time.sleep(poll_interval)

def main():
	print('INFURA key: {}'.format(os.environ.get("INFURA_API_KEY_MAIN")))
	loop_main(2)

main()
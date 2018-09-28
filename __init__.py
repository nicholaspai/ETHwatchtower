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
	INFURA_API_KEY_MAIN = os.environ.get("INFURA_API_KEY_MAIN")
	print('INFURA KEY: ' + INFURA_API_KEY_MAIN)
	loop_main(2)

main()
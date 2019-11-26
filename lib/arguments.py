import argparse

def get_args():
	parser = argparse.ArgumentParser(description="Monitor subdomains for changes.")
	parser.add_argument("-d", "--domain", metavar="", help="Domain to monitor")
	parser.add_argument("-n", "--name", metavar="", help="Name of the database file")
	args = parser.parse_args()

	if not any(vars(args).values()):
		parser.print_help()
		quit()
	else:
		return args
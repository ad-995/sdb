import argparse

def get_args():
	parser = argparse.ArgumentParser(description="Monitor subdomains for changes.")
	parser.add_argument("-d", "--domain", metavar="", help="Domain to monitor")
	parser.add_argument("-n", "--name", metavar="", help="Name of the database file")
	parser.add_argument("-i", "--interval",type=int, metavar="",default=30, help="Seconds between runs. 3 hrs = 10800")
	parser.add_argument("-t", "--threads",type=int, metavar="",default=10, help="Amount of threads to use, 10 by default")
	parser.add_argument("-s","--silent", action="store_true", help="Turn console output off")
	parser.add_argument("-q","--query", action="store_true", help="Extract all subdomains")
	parser.add_argument("--single", action="store_true", help="Run sdb once")
	parser.add_argument("--probe", action="store_true", help="Send HTTP Probes to each subdomain on a set of ports")
	args = parser.parse_args()

	if not any(vars(args).values()):
		parser.print_help()
		quit()
	else:
		return args
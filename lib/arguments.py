import argparse

def get_args():
	parser = argparse.ArgumentParser(description="Test.")
	parser.add_argument("-d", "--domain", metavar="", help="domain")
	parser.add_argument("-n", "--name", metavar="", help="db name")
	args = parser.parse_args()
	return args
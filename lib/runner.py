from lib.scanners import crtsh, bufferoverrun
from lib import db
from lib import crunch
from lib import arguments

args = arguments.get_args()
domain = args.domain

def verify(crunched_data):
	if crunched_data == None:
		logger.red('sdb was unable to retrieve data, check the logs!')
		return False
	else:
		logger.green('Successfully pulled data!')
		return True


def do_crtsh():
	crtsh_api = crtsh.api() # create an instance of the crtsh class. isnt really required but it was just incase multiple domains were going to be added

	domain_data = crtsh_api.search(domain) # go to crtsh and return a tuple. index 0 being the 'source' string, and 1 being the json blob.

	crunched_data = crunch.get_crtsh_data(domain_data)

	if verify(crunched_data):
		db.insert(crunched_data)
		return crunched_data
	else:
		return False


def do_bufferoverrun():
	bufferoverrun_api = bufferoverrun.api()

	domain_data = bufferoverrun_api.search(domain)

	crunched_data = crunch.get_bufferoverrun_data(domain_data)

	db.insert(crunched_data)

	if verify(crunched_data):
		db.insert(crunched_data)
		return crunched_data
	else:
		return False

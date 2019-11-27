from lib.scanners import crtsh, bufferoverrun, certspotter
from lib import db
from lib import crunch
from lib import arguments
from lib import logger

args = arguments.get_args()
domain = args.domain

def verify(data):
	if data == None:
		return False
	else:
		return True

# Both api calls will return None if they failed to do something, this is so they can be verified with the above

def do_crtsh():
	crtsh_api = crtsh.api() # create an instance of the crtsh class. isnt really required but it was just incase multiple domains were going to be added

	domain_data = crtsh_api.search(domain) # go to crtsh and return a tuple. index 0 being the 'source' string, and 1 being the json blob.

	if not verify(domain_data):
		logger.red('Failed to obtain data from %s' % logger.RED('crt.sh'))
		return False
	else:
		logger.green('Successfully validated %s response' % logger.GREEN('crt.sh'))

	crunched_data = crunch.get_crtsh_data(domain_data)

	if verify(crunched_data):
		db.insert(crunched_data)
		return crunched_data
	else:
		return False

def do_bufferoverrun():
	bufferoverrun_api = bufferoverrun.api()

	domain_data = bufferoverrun_api.search(domain)

	if not verify(domain_data):
		logger.red('Failed to obtain data from %s' % logger.RED('bufferover.run'))
		return False
	else:
		logger.green('Successfully validated %s response' % logger.GREEN('bufferover.run'))

	crunched_data = crunch.get_bufferoverrun_data(domain_data)

	if verify(crunched_data):
		db.insert(crunched_data)
		return crunched_data
	else:
		return False

def do_certspotter():
	certspotter_api = certspotter.api()

	domain_data = certspotter_api.search(domain)

	if not verify(domain_data):
		logger.red('Failed to obtain data from %s' % logger.RED('certspotter'))
		return False
	else:
		logger.green('Successfully validated %s response' % logger.GREEN('certspotter'))

	crunched_data = crunch.get_certspotter_data(domain_data)

	if verify(crunched_data):
		db.insert(crunched_data)
		return crunched_data
	else:
		return False

def go():
	logger.yellow('Checking %s' % 'crt.sh')
	do_crtsh()

	logger.yellow('Checking %s' % 'bufferover.run')
	do_bufferoverrun()

	logger.yellow('Checking %s' % 'certspotter')
	do_certspotter()
#!/usr/bin/python3
from lib import arguments
from lib import runner
from lib import db
from lib import logger
from time import sleep

args = arguments.get_args() # this function returns the args object

if args.domain == None:
	print('Please supply a domain')
	quit()
else:
	domain = args.domain
	if args.name != None:
		db.db_name = args.name
	db.init() # create the database file

counter = 0
interval = 3

logger.blue('Querying for subdomains every %s second(s)' % logger.BLUE(interval))

try:
	while True:
		sleep(1)
		counter += 1
		if counter == interval:
			logger.yellow('Checking %s' % 'crt.sh')
			runner.do_crtsh()

			logger.yellow('Checking %s' % 'bufferover.run')
			runner.do_bufferoverrun()
			counter = 0
except KeyboardInterrupt as e:
	logger.red('CTRL+C Detected!')
	quit()

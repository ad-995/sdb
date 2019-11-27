#!/usr/bin/python3
from lib import arguments
from lib import runner
from lib import db
from lib import logger
from lib import banner
from time import sleep

VERSION='0.2'

args = arguments.get_args() # this function returns the args object

banner.header(VERSION)

if args.domain == None:
	print('Please supply a domain')
	quit()
else:
	domain = args.domain
	if args.name != None:
		db.db_name = args.name
	db.init() # create the database file

interval = 30
counter = interval


try:
	while True:
		sleep(1)
		counter -= 1
		logger.timer('Querying in %s seconds(s)' % logger.BLUE(counter))
		if counter <= 0:
			logger.yellow('Checking %s' % 'crt.sh')
			runner.do_crtsh()

			logger.yellow('Checking %s' % 'bufferover.run')
			runner.do_bufferoverrun()

			logger.yellow('Checking %s' % 'certspotter')
			runner.do_certspotter()
			counter = interval

	
except KeyboardInterrupt as e:
	logger.red('CTRL+C Detected!')
	quit()

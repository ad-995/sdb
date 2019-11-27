#!/usr/bin/python3
from lib import arguments
from lib import runner
from lib import db
from lib import logger
from lib import banner
from time import sleep

VERSION='0.4'

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

if not args.query:
	if not args.single:
		try:
			while True:
				sleep(1)
				counter -= 1
				logger.timer('Querying in %s seconds(s)' % logger.BLUE(counter))
				if counter <= 0:
					runner.go()
					counter = interval

		except KeyboardInterrupt as e:
			logger.red('CTRL+C Detected!')
			quit()
	else:
		runner.go()
		log_results = db.log_results(db.query())
		quit()
else:
	log_results = db.log_results(db.query())
	quit()
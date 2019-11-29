#!/usr/bin/python3
from lib import arguments
from lib import runner
from lib import db
from lib import logger
from lib import banner
from lib import probe
from time import sleep

VERSION='0.5'

args = arguments.get_args() # this function returns the args object

if not args.silent:
	banner.header(VERSION)

if args.domain == None:
	logger.red('Please supply a domain')
	quit()
else:
	domain = args.domain
	if args.name != None:
		db.db_name = args.name
	db.init() # create the database file

interval = args.interval
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
		subdomains,wildcards = db.query()

		if args.probe:
			logger.yellow('Running HTTP probe')
			sleep(3)
			probed = probe.do(subdomains,args.threads)

		if args.probe:
			log_results = db.log_results((subdomains,wildcards),probed)
		else:
			log_results = db.log_results((subdomains,wildcards),None)
		quit()
else:
	log_results = db.log_results(db.query())
	quit()
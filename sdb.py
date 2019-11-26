#!/usr/bin/python3
from lib import arguments
from lib import runner
from lib import db
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

while True:
	sleep(1)
	counter += 1
	if counter == 30:
		runner.do_crtsh()
		counter = 0
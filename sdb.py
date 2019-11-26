#!/usr/bin/python3
from lib import arguments

args = arguments.get_args()

if args.domain == None:
	print('Please supply a domain')
	quit()
else:
	domain = args.domain
	print(domain)
	from lib import db
	if args.name != None:
		db.db_name = args.name
	db.init()


try:
	from tinydb import TinyDB, Query
except Exception as e:
	print(e)
	quit()
from lib import logger
import json, os

db_name = str('subdomains.db')

def init():
	if not os.path.isfile(db_name):
		logger.yellow('Creating database [%s]' % logger.YELLOW(db_name))
	db = TinyDB(db_name)
	return db

def insert(domain_data):
	db = init()
	data = vars(domain_data)
	logger.yellow('Adding %s to %s' % (logger.YELLOW(str(data)),logger.YELLOW(db_name)))
	try:
		db.insert(data)
	except Exception as e:
		logger.red(e)
		return None # this return code wont be checked anywhere, i just dont like leaving unclosed functions :)

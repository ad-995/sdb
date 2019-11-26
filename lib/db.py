from tinydb import TinyDB, Query
import json

db_name = str('db.json')

def init():
	db = TinyDB(db_name)
	return db

def insert(domain_data):
	db = init()
	# try:
	print(type(domain_data))
	# data = json.dumps(domain_data)
	# print(type(data))
	# except:
	# 	print('Failed to insert into database')
	# 	exit()

	db.insert(vars(domain_data))

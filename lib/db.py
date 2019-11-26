from tinydb import TinyDB, Query

db_name = str('db.json')

def init():
	db = TinyDB(db_name)

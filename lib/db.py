from lib import logger
from lib import arguments
from time import gmtime, strftime
import json, os, hashlib

try:
	from tinydb import TinyDB, Query
except Exception as e:
	logger.red('Got [%s] whilst importing %s' % logger.RED(str(e)),logger.RED('tinydb'))
	quit()

db_name = str('subdomains.db')

args = arguments.get_args()

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
		logger.red('Got [%s] whilst adding %s to %s' % (logger.RED(str(e)),logger.RED(data),logger.RED(db_name)))
		return None # this return code wont be checked anywhere, i just dont like leaving unclosed functions :)

def query():
	subdomains = []
	wildcards = []
	# https://tinydb.readthedocs.io/en/latest/getting-started.html
	db = init()
	q = Query()
	for counter,item in enumerate(db):
		uid = item['identifier']
		source = item['source']
		time = item['time']
		subdomain_set = item['domains']
		for subdomain in subdomain_set:
			if '*' in subdomain and subdomain not in wildcards:
				wildcards.append(subdomain)
			if '*' not in subdomain and subdomain not in subdomains:
				subdomains.append(subdomain)
	return subdomains,wildcards

def get_uid():
	log_time=strftime("%d/%m/%y %H:%M:%S", gmtime())
	uid = hashlib.md5(log_time.encode('utf-8')).hexdigest()
	return uid

def log_results(results_data,probed):
	subdomains = results_data[0]
	wildcards = results_data[1]
	uid = get_uid()

	if probed != None:
		try:
			filename = '%s_probed_%s.txt' % (args.domain,uid)
			with open(filename,'w') as f:
				logger.green('Writing wildcards to %s' % logger.GREEN(filename))
				for subdomain in probed:
					f.write(subdomain+'\n')
		except Exception as e:
			logger.red('Got [%s] whilst logging to %s' % (logger.RED(str(e)),logger.RED(filename)))
			return False
	try:
		filename = '%s_subdomains_%s.txt' % (args.domain,uid)
		with open(filename,'w') as f:
			logger.green('Writing subdomains to %s' % logger.GREEN(filename))
			for subdomain in subdomains:
				f.write(subdomain+'\n')
	except  Exception as e:
		logger.red('Got [%s] whilst logging to %s' % (logger.RED(str(e)),logger.RED(filename)))
		return False

	try:
		filename = '%s_wildcards_%s.txt' % (args.domain,uid)
		logger.green('Writing wildcards to %s' % logger.GREEN(filename))
		with open(filename,'w') as f:
			for wildcard in wildcards:
				f.write(wildcard+'\n')
	except  Exception as e:
		logger.red('Got [%s] whilst logging to %s' % (logger.RED(str(e)),logger.RED(filename)))
		return False
	return subdomains,wildcards

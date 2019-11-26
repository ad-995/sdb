import json, hashlib
from lib import domain_structure
from time import gmtime, strftime

def get_uid():
	log_time=strftime("%d/%m/%y %H:%M:%S", gmtime())
	uid = hashlib.md5(log_time.encode('utf-8')).hexdigest()
	return uid

def get_crtsh_data(domain_data):
	log_time=strftime("%d/%m/%y %H:%M:%S", gmtime())
	subdomains = []
	source = domain_data[0]
	json_blob = domain_data[1]
	for item in json_blob:
		item = dict(item)
		name_value = item['name_value']
		if not name_value.startswith('*'):
			if name_value not in subdomains:
				subdomains.append(name_value)
	domain = domain_structure.Domain(get_uid(),source,log_time,subdomains)
	return domain

def get_bufferoverrun_data(domain_data):
	log_time=strftime("%d/%m/%y %H:%M:%S", gmtime())
	subdomains = []
	source = domain_data[0]
	json_blob = domain_data[1]
	list_blob = list(json_blob['FDNS_A'])
	for i in list_blob:
		if ',' in i:
			if i.split(',')[0] not in subdomains:
				subdomains.append(i.split(',')[0])

			if i.split(',')[1] not in subdomains:
				subdomains.append(i.split(',')[1])
		else:
			if i not in subdomains:
				subdomains.append(i)

	domain = domain_structure.Domain(get_uid(),source,log_time,subdomains)
	return domain
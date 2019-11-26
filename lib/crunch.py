import json, hashlib
from lib import domain_structure
from time import gmtime, strftime

def get_data(domain_data):
	log_time=strftime("%d/%m/%y %H:%M:%S", gmtime())
	# print(json.dumps(domain_data, indent=4, sort_keys=True))
	subdomains = []
	source = domain_data[0]
	json_blob = domain_data[1]
	for item in json_blob:
		item = dict(item)
		name_value = item['name_value']
		if not name_value.startswith('*'):
			if name_value not in subdomains:
				subdomains.append(name_value)
	identifer = hashlib.md5(log_time.encode('utf-8')).hexdigest()
	domain = domain_structure.Domain(identifer,source,log_time,subdomains)
	return domain

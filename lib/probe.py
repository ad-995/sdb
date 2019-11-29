#!/usr/bin/python3
from lib import logger
import requests
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ports = [80,81,82,8080,8081,8082,8443,443,4443,8888,5601,9200,9201,9202]

def get_urls(subdomains):
	urls = []
	for subdomain in subdomains:
		for port in ports:
			if port == 80:
				url = 'http://%s' % subdomain
			elif port == 81 or port == 82:
				url = 'http://%s:%s' % (subdomain,port)
			elif port == 443:
				url = 'https://%s' % subdomain
			else:
				url = 'https://%s:%s' % (subdomain,port)
			urls.append(url)
	return urls

# split a list into evenly sized chunks
def chunks(users, chunk_size):
	if chunk_size == 0:
		chunk_size = 1
	return [users[i:i+chunk_size] for i in range(0, len(users), chunk_size)]

def check(urls):
	probed = []
	for url in urls:
		try:
			response = requests.get(url,allow_redirects=False,timeout=5,verify=False)
			logger.green('%s [%s]' % (url,logger.GREEN(response.status_code)))
			probed.append(url)
		except requests.exceptions.Timeout:
			logger.red('%s [%s]' % (url,logger.RED('Timed out')))
		except requests.exceptions.TooManyRedirects:
		    logger.red('%s [%s]' % (url,logger.RED('Too many redirects')))
		except requests.exceptions.RequestException as e:
		    logger.red('%s [%s]' % (url,logger.RED('Connection Refused')))
	return probed

def do(subdomains,processes):
	urls = get_urls(subdomains)

	total = len(urls)
	chunk_size = int(total / processes) # divide it by the amount of processes
	slice = chunks(urls, chunk_size) # evenly cut up the list

	probed = []
	with Pool(processes) as p:
		results = p.map(check, slice)
		for result in results:
			for url in result:
				if url not in probed:
					probed.append(url)
	return probed
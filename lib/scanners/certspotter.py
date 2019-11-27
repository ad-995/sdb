import requests, json
from lib import logger

class api:

	def search(self, domain):
		url = "https://api.certspotter.com/v1/issuances?domain=%s&expand=dns_names&expand=issuer&expand=cert" % domain
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
		try:
			response = requests.get(url, headers={'User-Agent': user_agent})
		except Exception as e:
			logger.red('Got [%s] whilst requesting %s' % (logger.RED(str(e)),logger.RED(url)))
			return None
		if response.ok:
			logger.green('Got [%s] from %s' % (logger.GREEN(response.status_code),logger.GREEN(url)))
			content = response.content.decode('utf-8')
			try:
				data = json.loads(response.text)
				return ('certspotter',data)
			except Exception as e:
				logger.red('Got [%s] whilst loading data from %s' % (logger.RED(str(e)),logger.RED(url)))
				return None
		else:
			return None
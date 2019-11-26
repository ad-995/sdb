import requests, json
from lib import logger

class api:

	def search(self, domain):
		url = "http://dns.bufferover.run/dns?q=%s" % domain
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
		try:
			response = requests.get(url, headers={'User-Agent': user_agent})
		except Exception as e:
			logger.red(e)
			return None
		if response.ok:
			logger.green('Got [%s] from %s' % (logger.GREEN(response.status_code),logger.GREEN(url)))
			content = response.content.decode('utf-8')
			try:
				data = json.loads(response.text)
				return ('dns.bufferover.run',data)
			except Exception as e:
				logger.red(e)
				return None
		else:
			logger.red('Got [%s] from %s' % (logger.RED(response.status_code),logger.RED(url)))
			return None
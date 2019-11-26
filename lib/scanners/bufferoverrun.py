import requests, json

class api:

	def search(self, domain):
		url = "http://dns.bufferover.run/dns?q=%s" % domain
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
		response = requests.get(url, headers={'User-Agent': user_agent})
		if response.ok:
			content = response.content.decode('utf-8')
			data = json.loads(response.text)
			return ('dns.bufferover.run',data)
		else:
			return None
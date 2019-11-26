import requests, json

class api:

    def search(self, domain, wildcard=True):
        base_url = "https://crt.sh/?q={}&output=json"
        if wildcard:
            domain = "%25.{}".format(domain)
        url = base_url.format(domain)

        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        response = requests.get(url, headers={'User-Agent': user_agent})

        if response.ok:
	        content = response.content.decode('utf-8')
	        data = json.loads(response.text)
	        return ('crtsh',data)
        else:
            return None
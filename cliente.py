import http.client
import urllib.request
import urllib.error

params = ''
url = 'http://127.0.0.1:7777/' + params

try:
    urllib.request.urlopen(url)
except http.client.HTTPException as e:
    print(e)
except urllib.error.URLError as e:
    print(e)

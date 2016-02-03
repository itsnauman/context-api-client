import requests
import json
import os

headers = {
    'content-type': 'application/json',
    'accept': 'application/json',
}

payload = {
    'username': os.getenv('CONTEXT_API_USERNAME', ''),
    'password': os.getenv('CONTEXT_API_PASSWORD', ''),
}

r = requests.post('https://context.newsai.org/api/jwt-token/',
                  headers=headers, data=json.dumps(payload), verify=False)
data = json.loads(r.text)
token = data['token']

headers = {
    'content-type': 'application/json',
    'accept': 'application/json',
    'authorization': 'JWT ' + token
}

payload = {
    'url': 'http://www.nytimes.com/2016/02/03/health/zika-sex-transmission-texas.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news&_r=0',
}

r = requests.post('https://context.newsai.org/api/articles/',
                  headers=headers, data=json.dumps(payload), verify=False)
data = json.loads(r.text)

print data

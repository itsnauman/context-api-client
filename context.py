import requests
import json
import os


def get_login_token():
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
    return r.json()['token']


def post_article(url):
    headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        'authorization': 'JWT ' + token
    }

    payload = {
        'url': url,
    }

    r = requests.post('https://context.newsai.org/api/articles/',
                      headers=headers, data=json.dumps(payload), verify=False)
    return r.json()

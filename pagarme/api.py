# coding=utf-8
import os
import re
import json
import requests

class Api(object):

	def __init__(self, api_key):
		self.api_key = api_key

	def headers(self):
		return {
			"Content-Type": "application/json",
			"Accept": "application/json"
		}

	def main_request(self, url, method, data={}):
		data['api_key'] = self.api_key
		try:
			response = requests.request(method, url,data=json.dumps(data),headers=self.headers())
			return json.loads(response.content.decode('utf-8'))
		except Exception as error:
			raise

	def get(self, url, data={}):
		return self.main_request(url, 'GET', data=data)

	def post(self, url, data={}):
		return self.main_request(url, 'POST', data=data)

	def put(self, url, data={}):
		return self.main_request(url, 'PUT', data=data)

	def delete(self, url):
		return self.main_request(url, 'DELETE')

	def get_url(self, paths):
		url = 'https://api.pagar.me/1'
		for path in paths:
			url = re.sub(r'/?$', re.sub(r'^/?', '/', str(path)), url)
		return url

__main_api__ = None

def main_api():

    global __main_api__
    if __main_api__ is None:
        __main_api__ = Api(api_key='TOKEN HERE')
    return __main_api__





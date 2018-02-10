#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from sys import exit

__version__ = '1.3.1'

class ViaCEP:

	def __init__(self, cep):
		self.cep = cep

	def getDadosCEP(self):
		url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
		try:
			req = requests.get(url_api)
			if req.status_code == 200:
				dados_json = json.loads(req.text)
				return dados_json
			else:
				exit("Status code error: %s" % req.status_code)
		except requests.exceptions.Timeout as err:
			print(err)
			exit(1)
		except requests.exceptions.TooManyRedirects as err:
			print(err)
			exit(1)
		except requests.exceptions.HTTPError as err:
			print(err)
			exit(1)
		except requests.exceptions.RequestException as err:
			print(err)
			exit(1)
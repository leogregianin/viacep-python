#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests

class ViaCEP:

    def __init__(self, cep):
        self.cep = cep

    def retorna_json_completo(self):
    	url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
    	req = requests.get(url_api)
    	dados_json = json.loads(req.text)
    	return dados_json

    def retorna_uf(self):
    	url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
    	req = requests.get(url_api)
    	dados_json = json.loads(req.text)
    	return dados_json['uf']

if __name__ == '__main__':
	test1 = ViaCEP('78048000')
	print(u'%s' % test1.retorna_json_completo())

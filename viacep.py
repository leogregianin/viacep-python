#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests

class ViaCEP:

    def __init__(self, cep):
        self.cep = cep

    def getDadosCEP(self):
    	url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
    	req = requests.get(url_api)
    	dados_json = json.loads(req.text)
    	return dados_json

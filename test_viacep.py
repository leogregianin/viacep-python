#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from viacep import ViaCEP

class TestCase(unittest.TestCase):

    def test_localidade(self):
        d = ViaCEP('78048000')
        data = d.getDadosCEP()
        self.assertEqual(data['localidade'], 'Cuiabá')

    def test_logradouro(self):
        d = ViaCEP('78048000')
        data = d.getDadosCEP()
        self.assertEqual(data['logradouro'], 'Avenida Miguel Sutil')

    def test_bairro(self):
        d = ViaCEP('78048000')
        data = d.getDadosCEP()
        self.assertEqual(data['bairro'], 'Alvorada')

    def test_uf(self):
        d = ViaCEP('78048000')
        data = d.getDadosCEP()
        self.assertEqual(data['uf'], 'MT')

    def test_ibge(self):
        d = ViaCEP('78048000')
        data = d.getDadosCEP()
        self.assertEqual(data['ibge'], '5103403')

    def test_01311200_ibge(self):
        d = ViaCEP('01311200')
        data = d.getDadosCEP()
        self.assertEqual(data['ibge'], '3550308')

    """
    def test_78048000_json(self):
        test_78048000 = u"{'cep': '78048-000', 'logradouro': 'Avenida Miguel Sutil', 'complemento': 'de 5686 a 6588 - lado par', 'bairro': 'Alvorada', 'localidade': 'Cuiabá', 'uf': 'MT', 'unidade': '', 'ibge': '5103403', 'gia': ''}"
        d = ViaCEP('78048000')
        data = d.getDadosCEP()
        self.assertEqual(data, test_78048000)

    def test_error(self):
        data_error = '{\'erro\': True}'
        d = ViaCEP('08048000')
        data = d.getDadosCEP()
        print(data)
        self.assertEqual(data, data_error)
    """

if __name__ == '__main__':
    unittest.main()

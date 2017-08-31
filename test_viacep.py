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

if __name__ == '__main__':
    unittest.main()

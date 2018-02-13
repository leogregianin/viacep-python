#!/usr/bin/python
# -*- coding: utf-8 -*-

from viacep import ViaCEP

data = ViaCEP('08048000')
print(u'%s' % data.getDadosCEP())
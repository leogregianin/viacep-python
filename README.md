# ViaCEP em Python

[![Build Status](https://travis-ci.org/leogregianin/viacep-python.svg)](https://travis-ci.org/leogregianin/viacep-python)

Buscar informações do CEP com o webservice do site http://www.viacep.com.br

## Pré requisitos

  * Instalação de qualquer versão do Python (http://www.python.org/download)
  
## Instalação das dependências

```bash
$ pip install -r requirements.txt
```

## Utilização

```bash
>>> import viacep
>>> d = viacep.ViaCEP('78048000')
>>> data = d.retorna_json_completo()
>>> data
{u'complemento': u'de 5799/5800 a 7887/7888', u'ibge': u'5103403', u'bairro': u'
Consil', u'logradouro': u'Avenida Miguel Sutil', u'unidade': u'', u'gia': u'', u
'cep': u'78048-000', u'uf': u'MT', u'localidade': u'Cuiab\xe1'}
>>> cidade = data['localidade']
>>> cidade
u'Cuiab\xe1'
>>> print(u'%s' % cidade)
Cuiabá
>>> uf = data['uf']
>>> uf
u'MT'
>>>
```

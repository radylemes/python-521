#!/usr/bin/python3

# Exibir apenas o logradouro -> ?

import requests

cep = input('Digite o CEP: ')

url = f'http://viacep.com.br/ws/{cep}/json/'
response = requests.get(url)

if response.status_code == 200:
    json = response.json()
    print(json['logradouro'])

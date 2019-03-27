#!/usr/bin/python3

from requests import post

nome = input('Digite o nome: ')
email = input('Digite o email: ')
idade = input('Digite a idade: ')

data = {'nome' : nome, 'email' : email, 'idade' : idade}
#data = {}
#data['nome'] = nome
#data['email'] = email
#data['idade'] = idade

response = post('http://192.168.202.79/usuarios', json=data)

print(response.text)

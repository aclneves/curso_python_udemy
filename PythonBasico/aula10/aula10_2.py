"""
Operadores Relacionais ==, >=. <, <= != com + IF/ELIF/ELSE
"""

nome = input('Digite o seu nome: ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo

idade_minima = 18
idade_maxima = 75


if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode pegar empréstimo!')
else:
    print(f'{nome} não pode pegar empréstimo!')
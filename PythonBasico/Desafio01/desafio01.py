"""
* Criar variáveis para nome (str), idade(int),
* altura(float) e peso (float) de uma pessoa
* Criar a variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
* Exibir o texto com todos os valors na tela usando F-Strings
"""
import datetime

nome = 'Antonio Neves'
idade = 33
altura = 1.79
peso = 84.5
ano_atual = 2021

ano_nascimento = ano_atual - idade
imc = peso/(altura ** 2)

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')




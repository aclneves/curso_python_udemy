"""
Entrada de dados
"""

nome = input('Digite o seu nome: ')
idade = input('Qual a sua idade: ')
ano_nascimento = 2021 - int(idade)

# Qualquer coisa que for recebida na função input é recebida como String

print(f'O usuário digitou {nome} e o tipo va variável é {type(nome)}')
print(f'{nome} tem {idade} anos de idade')
print(f'{nome} nasceu em {ano_nascimento}')

# Como abaixo os dois inputs receberão str, será concatenado ao invés de somar

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(numero_1 + numero_2)

# Para realizar a soma, deve ser feito o cast

num_1 = int(input('Digite um numero: '))
num_2 = input('Digite outro numero: ')
num_2 = int(num_2)
print(num_1 + num_2)

"""
Introdução a formatação de aula03
"""

nome = 'Antonio Neves'
idade = 33
altura = 1.79
e_maior = idade >= 18
peso = 84.5
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)

# Podemos utilizar f strings para escrever o mesmo texto

print(f'{nome} tem {idade} anos de idade e o seu IMC é {imc:.2f}')

# Podemos usar outra forma também

print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))

# Podemos também usar o índica ou os parâmetros com format

print('Com {1} anos de idade, {0} tem o IMC igual a {2:.2f}'.format(nome, idade, imc))

print('Com {i} anos de idade, {n} tem o IMC igual a {im:.2f}'.format(n=nome, i=idade, im=imc))

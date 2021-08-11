"""
Variáveis:

Iniciar com letra, pode conter números, separar com _, letas minúsculas
"""

nome = 'Antonio'
print(nome, type(nome))  # Como Python é de tipagem dinâmica, você não precisa definir o tipo quando declarar
idade = 32  # int
altura = 1.79  # float
e_maior = idade >= 18  # bool
peso = 84.5

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print('Idade x altura:', idade * altura)

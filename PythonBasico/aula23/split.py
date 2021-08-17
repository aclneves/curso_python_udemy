"""
Split, Join, Enumertate em Python
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # list
"""

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista = string.split(' ')  # O que divide a String é definido dentro das aspas
lista2 = string.split(',')

print(lista)
print(lista2)

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista2:
    print(valor.strip().capitalize())

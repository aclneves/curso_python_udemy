"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

print(lista[0])
print(lista[-5])  # Os dois comandos imprimem a mesma coisa, pois também existe o índice negativo

print(lista)  # Imprime toda a lista

# Modificando um valor da lista

lista[4] = 'F'

print(lista)

# As listas também suportam fatiamentp

print(lista[0:3])
print(lista[::2])

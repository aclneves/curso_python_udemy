"""
Enumerate - Enumerar elementos da lista # lista
"""

lista = [
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'José'],  # 1
    ['Helena', 'Edu', 'Lucas']  # 2
    ]

# Como são listas dentro de listas, a lista interior tem uma lista também
# então podemos pegar o Aline por exemplo seria um print(lista[1][1]

print(lista[1][1])

print(lista[1])

enumerada = enumerate(lista)
print(enumerada)  # Ele vai apenas mostrar a referência de memória, é um objeto iterável

print(list(enumerada))

print()
print('#############################################')
print()

enumerada = list(enumerate(lista))

print(enumerada[1][1][2])



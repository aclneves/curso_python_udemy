lista = ['Brasil', 'EUA', 'Canada', 'Argentina', 'Inglaterra']

for v1, v2 in enumerate(lista):
    print(v1, v2)

lista2 = [
    [0, 'Luiz'],
    [1, 'Maria'],
    [2, 'Jose']
]

print()

for indice, nome in lista2:  # O enumerate faz isso, ele gera um índice para a lista, sem precisar usar uma lista dentro
    print(indice, nome)

print()

n1, n2, n3, n4, n5 = lista  # Desempacotamento da primeira lista

print(n2)
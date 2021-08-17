lista1 = list(range(0, 100,8))

print(lista1)

soma = 0
for valor in lista1:
    soma += valor

print(soma)

lista2 = ['Antonio', True, 10, 20.4]

for elem in lista2:
    print(f'O tipo de {elem} é {type(elem)}')


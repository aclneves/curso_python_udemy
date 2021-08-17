"""
Desempacotamento de listas em Python
"""

lista = ['Real Madrid', 'Chelsea', 'Juventus']

n1, n2, n3 = lista  # Se não tiver a quantidade identica para desempacotar, dá erro, 3 variáveis, 3 valores


print(n1)
print(n2)
print(n3)
print()

lista2 = ['Real Madrid', 'Chelsea', 'Juventus', 'Barcelona', 'PSG', 'Liverpol', 'Borussia']

n1, n2, *outros = lista2  # Uma soluição para pegar só os dois primeitos valores, gera uma outra lista com o restante

print(n1)
print(n2)
print(outros)
print()

n1, n2, *outros, ultimo = lista2  # Pegar o último valor

print(n1)
print(n2)
print(outros)
print(ultimo)
print()

*primeiro, u3, u2, u1 = lista2  # Pegar os primeiros valores

print(u3)
print(u2)
print(u1)
print()

n1, n2, *_ = lista2  # O *_ siginifica que você não se importa com o resto, é uma convenção

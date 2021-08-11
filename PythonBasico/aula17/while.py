"""
While em Python - Aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira
"""

x = 0
while x < 5:
    print(x)
    x = x + 1

print('Acabou!\n')

x = 0

# Continue

while x < 5:
    if x == 3:
        x = x + 1
        continue  # O continue ele não executa o laço, neste caso não vai imprimir o 3
    print(x)
    x = x + 1

print()
# Break

x = 0

while x < 5:
    if x == 3:
        break
    print(x)
    x = x + 1



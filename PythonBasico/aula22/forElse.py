"""
For / Else em Python
"""

lista = ['Banana', 'Laranja', 'Tangerina']

comeca_com_B = False

for valor in lista:
    if valor.lower().startswith('b'):
        print('Começa com B', valor)
    else:
        print('Não começa com B', valor)

print()

for valor in lista:
    if valor.startswith('M'):
        comeca_com_B = True
        print('Existe uma palavra que começa com M')
        break
else:
    print('Não existe uma palavra que começa com M')
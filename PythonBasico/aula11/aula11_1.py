"""
Operadores Lógicos
and, or, not
in e not in
"""

x = 2
y = 2
z = 3

teste_and = (x == y and x < z)  # As duas comparações precisam ser verdadeiras para retornar Trues
print(teste_and)

teste_or = (x == y or x > z)  # Apenas uma comparação precisa ser verdadeira para retonrar True
print(teste_or)

a = 2
b = 3

if not b > a:
    print('A é maior que B')
else:
    print('B é maior que A')

# Uitliza-se o note muito para checar se uma variável está vazia

nome = ''

if not nome:
    print('Por favor preecha um nome!')

# in e not in é utilizado para pesquisar se um elemento existe ou não existe em um vetor, lista ou str

nome = 'Antonio'

if 'o' in nome:
    print('Existe a letra O no seu nome')

if 'j' not in nome:
    print('Não existe a letra J no seu nome')


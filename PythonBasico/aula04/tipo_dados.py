"""
Tipos de dados
str - string - textos
int - inteiro - 123456, 0, -20, 1500, 233
float - real/ponto flutuante - 0.0, 1.1, -5.3
bool - booleano/lógico - true, false 10 == 10
"""
# O type retorna o tipo do dado passado como parâmetro

print('Antonio',type('Antonio'))
print(25,type(25))
print(15.2, type(15.2))
print(10 == 10, type(10 == 10))
print('L' == 'l', type('L' == 'l'))

# Nem sempre o booleano precisa ser uma comparação, por exemplo algumas coisas retornam false, como uma string vazia

print(bool(''))
print(bool(0))
print(bool([]))

# Casting

print('Antonio', type('Antonio'), bool('Antonio'))
print('10', type('10'), type(int('10')))

# print('Antonio', int('Antonio')) não pode ser feito, pois não dá para converter uma String em inteiro,a não ser qu
# seja um número

print(float('10.5'))
print(float(10))

# Quando se soma dois números é feita a soma, já quando se usa com uma String, são concatenadas

print(10 + 10)
print('10' + '10')




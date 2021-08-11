"""
Operadores Relacionais ==, >=. <, <= != com + IF/ELIF/ELSE
"""

print(2 == 2)  # True
print(2 == 1)  # False
print(2 == '2')  # False, pois int != str

num_1 = 4
num_2 = 2

iguais = (num_1 == num_2)
print(iguais)

maior_que = (num_1 > num_2)
print(maior_que)

maior_igual = (num_1 >= num_2)
print(maior_igual)

menor = (num_1 < num_2)
print(menor)

menor_igual = (num_1 <= num_2)
print(menor_igual)

diferente = (num_1 != num_2)
print(diferente)

"""
isdecimal(), isdigit(), isnumeric()
"""

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
# print(is_float('-101.0112'))  # True
# Int
# print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
# print(is_number('-1010.112'))  # True

# print(is_number('123a'))  # False


num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# Essas funções retornam um booleano mostrando se pode ser convertido para número ou não
# Essa funções só vão verificar se os números são inteiros e positivos, se for passado um negativo ou float não
# vai funcionar

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não foi digitado um número.')

# Utilizando as funções construiídas em cima

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)

else:
    print("Não foi digitado um número")


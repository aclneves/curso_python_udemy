"""
Operadores aritiméticos em Python

+ - Adição
- - Subtração
* - Multiplicação
/ - Divisão
// - Divisão inteiro
** - Exponenciação
% - Módulo, resto da divisão
() - Usados para alterar precedência das contas
"""

print('Adição', 10 + 10)
print('Multiplicação', 10 + 10)
print('Subtração', 10 - 5)
print('Divisão', 10 / 2)  # A divisão sempre retorna um float

# Os operadores + e * também podem ser utilizados em string

print('Concatenação de string: ', 'Antonio' + ' ' + 'Neves')
print('Repetição de string: ', 3 * 'Repetir ')

print('Divisão inteira: ', 10.5 // 3)  # Se foram dois int vai retornar um int, se float retona um float

print('Exponenciação', 3 ** 3)
print('Resto da divisão', 10 % 3)

# Utilizando parênteses

print(10 * 2 + 5)  # 25
print(10 * (2 + 5))  # 70

print(2 + 5 * 3 ** 2 - (23.5 + 23.5))


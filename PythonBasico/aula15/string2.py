"""
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

nome = "antonio"
sobrenome = "neves"

nome_comnpleto = '{0} {1}'.format(nome, sobrenome)

print(nome_comnpleto)

print(nome_comnpleto.upper())
print(nome_comnpleto.lower())
print(nome_comnpleto.title())

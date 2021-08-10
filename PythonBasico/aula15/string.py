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

nome = "Antonio Neves"
print(f'{nome:#^50}')

nome_formatado = '{:@>20}'.format(nome)
nome_formatado_2 = '{n}{n}{n}{n}'.format(n=nome)

print(nome_formatado)

print(nome_formatado_2)



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

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print(divisao)  # Imprimirá 3.333333333...

# Format
print("Usando format")
print("{:.2f}".format(divisao))

# F strings
print(f"{divisao:.2f}")

print(f'{num_1:0>10}')  # Inclui a quantidade do caracter espeficificado até completar o tamanho determinado

print(f'{num_1:.2f}')  # Coloca casas decimais mesmo sendo inteiro

print(f'{num_1:0>10.2f}')  # Podemos combinar os dois



"""
Manipulando Strings
* String índices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len. abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""

texto = "Python_S2"  # As strings tem índices positivos e negativos

print(texto[2])
print(texto[-1])

url = "www.google.com.br/"

print(url[:-1])

# Fatiamento de strings

nova_string = texto[2:6]  # O fim do fatiamento não é incluído
print(nova_string)

nova_string = texto[:6]  # Se não for passado nada, começa do primeiro elemento
print(nova_string)

nova_string = texto[7:]  # Analogamente, o final vazio ele faz até o fim da string
print(nova_string)

nova_string = texto[-9:-3]  # Usando negativos
print(nova_string)

# Pulando caracteres usando step

nova_string = texto[0::2]
print(nova_string)

print(len(texto))

for letra in texto:
    print(letra)
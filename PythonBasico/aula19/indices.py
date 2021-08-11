# Índices
# Geralmente se usa for para fazer isso, mas estamos usando o while

frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

escolha = input("Qual letra deseja colocar maíuscula: ")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == escolha:
        nova_string += escolha.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)





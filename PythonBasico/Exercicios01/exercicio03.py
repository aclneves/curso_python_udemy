"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 7 letras, escreva "Seu nome é normal"; se tiver 7 letras ou mais escreva "Seu nome é grande".
"""
nome = input("Por favor escreva o seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto")
elif tamanho <= 7:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")

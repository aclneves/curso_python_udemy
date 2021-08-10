"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o
usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num = input("Por favor digite um número inteiro: ")

if num.isdigit():

    num = int(num)

    if num % 2 == 0:
        print(f"{num} é par!")
    else:
        print(f"{num} é ímpar!")
else:
    print("Não foi digitado um número inteiro!")

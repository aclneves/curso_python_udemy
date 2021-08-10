"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada
Bom dia! - Entre 0 e 11
Boa tarde! - Entre 12 e 17
Boa noite! - Entre 18 e 23
"""

hora = (input("Que horas são? "))

if hora.isdigit():

    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Não foi digitada uma hora correta!")
    else:
        if hora <= 11:
            print("Bom dia!")
        elif hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")

else:
    print("Não foi digitado um número!")


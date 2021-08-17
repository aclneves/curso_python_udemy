secreto = 'perfume'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Infelizmente você perdeu!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Não vale, digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Você acertou, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta')
        digitadas.pop()
        chances -= 1

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Parabéns, você ganhou! A palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    print(f'Você ainda tem {chances} vidas!')
    print()

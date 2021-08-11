texto = 'I love Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
    elif letra == 'n':
        break
    else:
        nova_string += letra

print(nova_string)

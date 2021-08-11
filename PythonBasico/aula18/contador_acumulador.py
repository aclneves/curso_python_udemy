"""
Whilhe / Else
Contadores
Acumuladores
"""

contador = 1  # garante que o while tem um fim
acumulador = 1

while contador <= 10:
    print(contador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else!')  # Não passa no Else porque não terminou o else, só passa se terminar

print(acumulador)
print('Isso será executado!')

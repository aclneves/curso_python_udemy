"""
Função len - Funciona com str e outros tipos
"""

usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)  # retorna um inteiro com a quantidade de caracteres

if qtd_caracteres < 6:
    print('O usuário precisa ter pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sitema')

string1 = input('Digite alguma acoisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade de caracteres digitados foi {len(string1) + len(string2)}')

# Tudo em Pyhton é tratado como um objeto, então muitas funções podem ser utilizadas, essa função len é uma delas
# que chama um método len, como pode ser feito assim

print(string1.__len__())

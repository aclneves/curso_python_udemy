"""
Operadores Lógicos
and, or, not
in e not in
"""

# Exemplo de um login

print('Login:')
usuario = input('Nome do usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'aclneves'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print(f'usuario {usuario} está logado no sitema')
else:
    print('Usuario ou senha incorretos')

nome = str(input('Escreva seu nome: ')).strip()

print(nome.upper())

print(nome.lower())

print('Seu nome completo tem', len(nome)-nome.count(' '), 'letras.')

print('Seu primeiro nome tem', len(nome.split()[0]), 'letras.')
frase = input('Escreva uma frase: ')

A = frase.count('A')
P = frase.find('A')
U = frase.rfind('A')

print('Sua frase tem', A, 'letras "A" e o primeiro aparece na casa', P, 'e o último na casa', U)

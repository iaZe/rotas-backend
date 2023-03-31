from random import randint
num = randint(0, 5)
print('Estou pensando em um número de 0 a 5, duvido você acertar! ')
escolha = int(input('Em qual número eu pensei? '))
if escolha == num:
    print('Parabéns, você acertou ')
else:
    print('Infelizmente você errou, eu pensei no número {}.'.format(num))
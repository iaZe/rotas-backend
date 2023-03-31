from random import randint
num = randint(0, 10)
chute = ''

print('Estou pensando em um número de 0 a 10, duvido você acertar! ')

while chute != num:
    chute = int(input('Em qual número estou pensando? '))

print('Você acertou! Eu estava pensando no número {}'.format(num))
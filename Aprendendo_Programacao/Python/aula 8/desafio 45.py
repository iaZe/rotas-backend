from random import randint

print('-=' * 11)
print('''
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura
''')
print('-=' * 11)
pl = int(input('Qual sua escolha? '))

itens = ('Pedra', 'Papel', 'Tesoura')

pc = randint(0, 2)

print('-=' * 11)
print('Joken Po!')
print('-=' * 11)
print('Você escolheu {}'.format(itens[pl]))
print('O computador escolheu {}'.format(itens[pc]))
print('-=' * 11)

if pc == 0: # Pedra
    if pl == 0:
        print('Empate!')
    
    elif pl == 1:
        print('Você ganhou')

    elif pl == 2:
        print('Você perdeu')
    
    else:
        print('Jogada invalida')

if pc == 1: #Papel
    if pl == 0:
        print('Você perdeu')

    elif pl == 1:
        print ('Empate')

    elif pl == 2:
        print('Você ganhou')

    else:
        print('Jogada invalida')

if pc == 2: #Tesoura
    if pl == 0:
        print('Você ganhou')
    
    elif pl == 1:
        print('Você perdeu')
    
    elif pl == 2:
        print('Empate')
    
    else:
        print('Jogada invalida')
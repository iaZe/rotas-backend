from random import randint
vit = 0
while True:
    esc = int(input('''[ 0 ] PAR
[ 1 ] IMPAR
Você quer: [0/1] '''))
    print('-=-' * 10)
    p1 = int(input('Qual seu número? (De 0 a 10) '))
    print('-=-' * 10)
    p2 = randint(0, 10)
    soma = p1 + p2
    if esc == 0:
        if soma % 2 == 0:
            print(f'Você ganhou, pois a soma foi {p1} + {p2} = {soma} que é par')
            vit += 1
        else:
            print(f'Você perdeu, pois a soma foi {p1} + {p2} = {soma} que é impar')
            break
    if esc == 1:
        if soma % 3 == 0:
            print(f'Você ganhou, pois a soma foi {p1} + {p2} = {soma} que é impar')
            vit += 1
        else:
            print(f'Você perdeu, pois a soma foi {p1} + {p2} = {soma} que é par')
            break
    print('-=-' * 10)
print(f'Você ganhou {vit} vezes')
print('=' * 22)
print(' 10 TERMOS DE UMA P.A')
print('=' * 22)
pri = int(input('[PRIMEIRO TERMO]: '))
raz = int(input('[RAZÃO]: '))
termo = pri
cont = 1

while cont <= 10:
    print('{} >> '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM')
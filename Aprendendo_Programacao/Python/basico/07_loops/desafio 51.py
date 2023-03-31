print('=' * 22)
print(' 10 TERMOS DE UMA PA')
print('=' * 22)

pri = int(input('Primeiro termo da PA: '))
raz = int(input('Razão da PA: '))
dec = pri + (10 - 1) * raz
for c in range(pri, dec, raz):
    print('{} '.format(c), end = ' >> ')
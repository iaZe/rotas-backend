n = int(input('Qual numero você quer a tabuada? '))
print('A tabuada de {} é: '.format(n))
for c in range(1,13):
    print('{} x {} = {}'.format(n, c, n*c))

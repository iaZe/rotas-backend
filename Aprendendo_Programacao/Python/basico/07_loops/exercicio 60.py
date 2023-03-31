from math import factorial
num = int(input('Qual número você gostaria de obter o fatorial? '))
c = num
fac = factorial(num)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(fac), end='')
    c -= 1
print('')
print('Obrigado')
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('', end = '')
        tot += 1
    else:
        print('', end = '')
    print('{} '.format(c), end = ' ')
    
print('O número {} é divísvel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('Por isso ele não é PRIMO')
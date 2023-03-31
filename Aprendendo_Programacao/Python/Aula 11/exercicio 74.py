from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)) # randint entre parenteses para tupla
print('Os valores foram: ', end='')
for num in n:
    print(f'{num} ', end='')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
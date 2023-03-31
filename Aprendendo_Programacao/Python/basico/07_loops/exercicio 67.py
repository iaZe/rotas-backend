n = 0
while True:
    n = int(input('Qual número você gostaria de ver a tabuada? '))
    if n < 0:
        break
    print(f'A tabuada de {n} é')
    for c in range(1,13):
        print(f'{n} x {c} = {n*c}')
print('Encerrando...')
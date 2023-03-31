lista = ('Lápis', 1.75,
        'Borracha', 2.0,
        'Caderno', 3.0,
        'Estojo', 10.0,
        'Mochila', 50.0)

print(f'{"LISTAGEM DE PREÇO":^35}')

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]}')
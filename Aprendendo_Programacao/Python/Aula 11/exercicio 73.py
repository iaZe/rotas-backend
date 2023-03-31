times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino',
        'Athletico-PR', 'Flamengo', 'Ceará SC', 'Bahia', 'Fluminense', 'Santos')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 3 últimos colocados são: {times[-3:]}')
print(f'Em ordem {sorted(times)}')
print(f'O Flamengo está na {times.index("Flamengo")+1}º posição ')
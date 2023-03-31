palavras = ('lobo', 'carro', 'casa', 'curso', 'video', 'aula')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
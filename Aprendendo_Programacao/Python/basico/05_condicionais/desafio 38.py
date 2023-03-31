a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a > b:
    print('O maior valor é {}'.format(a))
elif b > a:
    print('O maior valor é {}'.format(b))
else:
    print('Os valores são iguais')
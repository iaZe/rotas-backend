r1 = float(input('Digite o valor da primeira reta '))
r2 = float(input('Digite o valor da segunda reta '))
r3 = float(input('Digite o valor da terceira reta '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    if r1 != r2 and r2 != r3 and r1 != r3: #diferente
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('As retas não formam um triangulo')
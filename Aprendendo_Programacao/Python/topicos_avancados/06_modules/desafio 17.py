from math import hypot
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(co, ca)))
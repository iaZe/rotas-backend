a = int(input('Escolha um número '))
b = int(input('Escolha outro número '))
c = int(input('Escolha mais um número '))

# Ver quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print('O menor valor digitado foi: {}'.format(menor))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor digitado foi: {}'.format(maior))

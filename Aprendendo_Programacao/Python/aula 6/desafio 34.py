sal = float(input('Qual valor do seu salário? '))

au1 = sal + (sal * 0.10)
au2 = sal + (sal * 0.15)

if sal >= 1250:
    print('Seu novo salário é R$ {}'.format(au1))
else:
    print('Seu novo salário é R$ {}'.format(au2))
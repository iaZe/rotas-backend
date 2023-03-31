idade = int(input('Qual a sua idade? '))

if idade == 17 and 18:
    print('Está na hora de se alistar')
elif idade > 18:
    print('Você está atrasado, se aliste o mais rapido possível')
else:
    falta = 18 - idade
    print('Ainda faltam {} anos para você se alistar'.format(falta))
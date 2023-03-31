n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))

med = (n1 + n2 ) / 2

if med >= 7:
    print('Você está aprovado com média: {}'.format(med))

elif med >= 5 and med < 7:
    print('Você está de recuperação com média: {}'.format(med))

elif med < 5:
    print('Você está reprovado com média: {}'.format(med))
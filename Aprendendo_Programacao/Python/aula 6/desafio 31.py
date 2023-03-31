km = int(input('Quantos km você viajou? '))
valor = (km * 0.50)
valor2 = (km * 0.45)

if km <= 200:
    print('O valor da sua viagem é de R${}.'.format(valor))
else:
    print('O valor da sua viagem é de R${}.'.format(valor2))
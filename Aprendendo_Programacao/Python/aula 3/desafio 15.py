day = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos km você usou o carro? '))
valor = (day * 60) + (km * 0.15)

print('O total a pagar é R${:.2f}'.format(valor))

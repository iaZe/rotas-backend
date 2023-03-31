valor = float(input('Digite o valor a ser pago: '))
print('Qual a forma de pagamento?\n 1 - À vista\n 2 - À vista no cartão\n 3 - Até 2x no cartão')
forma = int(input(' 4 - 3x ou mais no cartão\n '))

f1 = valor - (valor * 0.10)
f2 = valor - (valor * 0.05)
f3 = valor
f4 = valor + (valor * 0.20)

if forma == 1:
    print('Você ganhou 10% de desconto! \n O valor total é de: R${}'.format(f1))
elif forma == 2:
    print('Você ganhou 5% de desconto! \n O valor total é de: R${}'.format(f2))
elif forma == 3:
    print('O valor total é de: R${}'.format(f3))
else:
    print('Para pagamentos parcelados acima de 3x temos um juros de 20% \n O valor total é de: R${}'.format(f4))
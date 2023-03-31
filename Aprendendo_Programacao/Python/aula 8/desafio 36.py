valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual valor do seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))

prest = valor / (anos * 12 )

if prest <= (sal - (sal * 0.30)):
    print('Emprestimo aprovado \n O valor da prestação será de {:.2f} por mês'.format(prest))
else:
    print('Emprestimo recusado, você não pode pagar {:.2f} por mês'.format(prest))
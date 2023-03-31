radar = int(input('Você passou no radar com quantos km/h? '))
valor = (radar - 80) * 7

if radar >= 80:
    print('Você foi multado!')
    print('O valor da sua multa é de {}'.format(valor))
else:
    print('Você não foi multado, parabéns')
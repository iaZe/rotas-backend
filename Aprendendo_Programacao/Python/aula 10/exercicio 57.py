sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Invalido, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Obrigado')
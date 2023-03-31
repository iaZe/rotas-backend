idade = int(input('Digite sua idade: '))

if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade <= 20:
    print('Você está na caregoria SÊNIOR')
else:
    print('Você está na categoria MASTER')
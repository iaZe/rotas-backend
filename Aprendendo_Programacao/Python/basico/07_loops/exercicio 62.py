print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >> '.format(termo), end='')
        termo += raz
        cont += 1
    print('END ')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Finalizando o programa')
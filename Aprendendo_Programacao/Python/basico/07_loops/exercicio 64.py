num = cont = soma = 0
num = int(input('Digite um número [PARA PARAR DIGITE 999]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [PARA PARAR DIGITE 999]: '))
print('Você digitou {} números, e a soma entre eles é {} '.format(cont, soma))
quant = soma = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    media = soma / quant
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

print('Você digitou {} números, a média entre eles foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
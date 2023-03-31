num = int(input('Qual número você gostaria de converter? '))
conv = int(input('Escolha: \n  1 para binário \n  2 para octal \n  3 para hexadecimal  \n - '))

if conv == 1:
    print('Seu número convertido para binário é: {}'.format(bin(num)))
elif conv == 2:
    print('Seu número convertido para octal é {}'.format(oct(num)))
elif conv == 3:
    print('Seu número convertido para hexadecimal é {}'.format(hex(num)))
else:
    print('Opção invalida, escolha uma das opções')
v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    print('''[1] SOMAR
[2] MUTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
''')

    opcao = int(input('Você gostaria de: '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma de {} + {} = {}'.format(v1, v2, soma))

    elif opcao == 2:
        produto = v1 * v2
        print('O resultado de {} x {} = {}'.format(v1, v2, produto))

    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, maior))

    elif opcao == 4:
        print('Informe os novos números')
        v1 = int(input('Primeiro número: '))
        v2 = int(input('Segundo número: '))
    
    elif opcao == 5:
        print('Finalizando')

    else:
        print('Opão invalida!')
    print('=-=' * 15)

print('Fim do programa!')
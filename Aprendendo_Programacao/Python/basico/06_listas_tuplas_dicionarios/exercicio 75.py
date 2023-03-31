
núm = (int(input('Digite um número ')),
    int(input('Digite um número ')),
    int(input('Digite um número ')),
    int(input('Digite um número '))
)

print(f'Você digitou os valores {núm}')

print(f'O valor nove apareceu {núm.count("9")} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {núm.index(3)+1}º posição' if 3 in núm else 'Não foi digitado valor 3')
print('Os valores pares digitados foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end='')

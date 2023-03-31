total = caro = menor = contar = 0
barato = ''

while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    contar += 1
    total += valor

    if valor > 1000: #produto mais caro
        caro += 1
    if contar == 1 or valor < menor: #produto mais barato
        menor = valor
        barato = nome

    resp = ' ' #função de continuar
    while resp not in 'SN':
        resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'''O valor total é R$ {total:.2f}
Foram comprados {caro} produtos acima de R$ 1000
O mais barato foi {barato} custando R${menor:.2f}''')
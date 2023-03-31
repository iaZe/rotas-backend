maior = homens = mulheres = quant = 0
while True:
    print('-='*25)
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: [M/F] ')).upper().strip()[0]
    print('-='*25)
    cont = str(input('Deseja cadastrar mais alguém? [S/N] ')).upper().strip()[0]
    quant += 1

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1
    if cont == 'N':
        break

print('-='*25)
print(f'''Foram cadastradas {quant} pessoas, sendo:
{maior} maiores de idade
{homens} homens
E {mulheres} mulheres tem menos de 20 anos''')
print('-='*25)
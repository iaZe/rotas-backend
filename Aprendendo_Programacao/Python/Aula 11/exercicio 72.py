tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')


while True:
    num = int(input('Digite um número [0 a 10]: '))
    if 0 <= num <= 20:
        break
    else:
        print('Digite um valor válido')
print(tupla[num])
n = soma = quant = 0
while True:
    n = int(input('Digite um número: [999 TO STOP]'))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'{quant} números foram digitados e a soma entre eles é {soma}')
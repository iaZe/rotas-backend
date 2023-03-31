peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? (Digite seguindo o exemplo: 1.75, 1.80: '))

imc = peso / (altura * altura)
print('Seu IMC equivale a:', imc)
if imc < 18.5:
    print('Você está abaixo do peso ')
elif imc < 25:
    print('Você está com o peso ideal ')
elif imc < 30:
    print('Você está no sobrepeso ')
elif imc < 40:
    print('Você está na obesidade ')
else:
    print('Você está na obesidade mórbida')

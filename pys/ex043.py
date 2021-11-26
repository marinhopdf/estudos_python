massa = float(input('Digite sua massa corporal em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = massa/(altura**2)

print(f'Seu IMC é {imc}.')

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
if imc >= 18.5 and imc < 25:
    print('Você está na faixa de peso ideal.')
if imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
if imc >= 30 and imc < 40:
    print('Vocẽ está obeso.')
if imc >= 40:
    print('Você está com obesidade mórbida.')
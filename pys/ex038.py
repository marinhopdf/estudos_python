numero1 = float(input('Digite o número 1: '))
numero2 = float(input('Digite o número 2: '))

if numero1 > numero2:
    print(f'O primeiro número ({numero1}) é maior que o segundo ({numero2})')
elif numero1 < numero2:
    print(f'O segundo número ({numero2}) é maior que o primeiro ({numero1})')
else:
    print('Os números informados são iguais.')

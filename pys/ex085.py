numeros = [[], []]
n = 0
for i in range(1, 8):
    n = int(input(f'Digite o {i}o número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(f'Os número pares foram {numeros[0]}')
print(f'Os números impares foram {numeros[1]}')
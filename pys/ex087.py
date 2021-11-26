matriz = [[0,0,0], [0,0,0], [0,0,0]]
n = 0
pares = []
terceira = []
segunda = []
for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Digite o valor da posição ({l},{c}): '))
        if n%2 == 0:
            pares.append(n)
        if l == 1:
            segunda.append(n)
        if c == 2:
            terceira.append(n)
        matriz[l][c] = n
print('A matriz inserida foi: ')
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares inseridos é igual a {sum(pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(terceira)}.')
print(f'O maior valor da segunda linha é {max(segunda)}.')
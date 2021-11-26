soma = 0
for i in range (1,7):
    print()
    n = float(input(f'Digite o número {i}: '))
    if n % 2 == 0:
        soma = n + soma
print(f'A soma dos números é {soma}.')



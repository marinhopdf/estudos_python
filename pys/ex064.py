n = int(input('Digite os números: '))
c = 1
soma = 0
while n != 999:
    n = int(input('Digite os números: '))
    c += 1
    soma = soma+n
print(f'A soma dos {c} números que você digitou é {soma}')
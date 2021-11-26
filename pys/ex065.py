n = int(input('Digite os números: '))
c = 1
soma = 0
menor = n
maior = n
while n != 999:
    n = int(input('Digite os números: '))
    if menor > n:
        menor = n
    if maior < n:
        maior = n
    c += 1
    soma = soma+n
media = (soma-999)/c
print(f'A soma dos {c} números que você digitou é {soma} e a média deles é {media}. O maior foi {maior} e o menor foi {menor}')
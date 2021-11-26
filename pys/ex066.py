n = int(input('Digite os números: '))
c = 1
soma = 0
menor = n
maior = n
while True:
    if n == 999:
        break
    n = int(input('Digite os números: '))
    if n == 999:
        break
    if menor > n:
        menor = n
    if maior < n:
        maior = n
    c += 1
    soma = soma+n
media = (soma)/c
print(f'A soma dos {c} números que você digitou é {soma} e a média deles é {media}. O maior foi {maior} e o menor foi {menor}')
soma = 0
count = 0
for i in range (1, 501, 2):
    if i%3 == 0:
        print(i, end=' ')
        soma = soma + i
        count = count + 1
print(f'Existem {count} números múltiplos de 3 entre 1 e 500 e a soma de todos eles é {soma}.')
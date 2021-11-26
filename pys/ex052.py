n = int(input('Digite um número para verificar se ele é primo: '))
count = 0
print(f'O númnero {n} é divisível pelos seguintes números: ')
for i in range (1, n+1):
    if n%i == 0:
        print(i, end=' ')
        count += 1
if count > 2:
    print(f'\n O número {n} não é primo.')
else:
    print(f'\n O número {n} é primo.')
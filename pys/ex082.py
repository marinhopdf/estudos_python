lista = []
pares = []
impares = []
while True:
    n = float(input('Digite um número: '))
    lista.append(n)
    chave = str(input('Deseja contunuar(S/N)? ').strip().upper())[0]
    if chave == 'N':
        break
for i in range(0, len(lista)):
    if lista[i]%2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
lista.sort()
pares.sort()
impares.sort()
print(f'Os números digitados foram: {lista}')
print(f'Os pares foram: {pares}')
print(f'Os imapares foram: {impares}')

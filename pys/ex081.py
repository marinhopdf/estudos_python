lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    chave = str(input('Deseja continuar (S/N)? ').upper().strip())[0]
    if chave == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort()
print(f'Os valores da lista foram {lista}')
if '5' in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')

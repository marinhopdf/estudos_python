lista = []
for i in range(0, 5):
    lista.append(float(input(f'Digite um número da posição {i}: ')))
print(f'O menor número digitado foi {min(lista)} e sua posição é {lista.index(min(lista))}.')
print(f'O maior número digitado foi {max(lista)} e sua posição é {lista.index(max(lista))}.')
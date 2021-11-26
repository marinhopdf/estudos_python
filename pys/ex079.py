numeros = []
i=0
while True:
    element = input(f'Informe o valor da posição {i}: ')
    i+=1
    if element not in numeros:
        numeros.append(element)
    else:
        chave = str(input('Elemento já está presente na lista. Deseja continuar? ').upper().strip())[0]
        if chave == 'N':
            break

print(numeros)
numeros.sort()
print(numeros)
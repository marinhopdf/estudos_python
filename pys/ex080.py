lista = []
for i in range (0,6):
    e = float(input(f'Digite o valor do elemento {i}: '))
    if i == 0 or e > lista[-1]:
        lista.append(e)
    else:
        pos = 0
        while pos < len(lista):
            if e <= lista[pos]:
                lista.insert(pos, e)
                break
            pos += 1
print(lista)
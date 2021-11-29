from random import randint

lista_n = []
contador = 0
parada = 0
numero = None

def randomico():
    numero = randint(1, 9999)
    lista_n.append(numero)


while True:
    contador += 1
    randomico()
    parada = randint(1, 9999)
    if contador >= parada:
        break

print(f'A lista com os elementos foi {sorted(lista_n)}')
print(f'O programa atribuiu {len(lista_n)} elementos à lista de números. O maior número dentre ele foi {max(lista_n)}')
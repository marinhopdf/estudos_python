from random import randint

def sorteio():
    numeros = []
    for i in range(0, 5):
        numeros.append(randint(1, 99))
    sorted(numeros)
    return numeros

def somaPar(sorteados):
    pares = [x for x in sorteados if x % 2 == 0]
    return sum(pares)


parada = int(input('Quantas vezes o programa será executado? '))

for i in range(parada):
    sorteados = sorteio()
    somas = somaPar(sorteados)

print(f'A soma da lista {sorteados} é {somas}.')

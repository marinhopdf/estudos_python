from random import randint
from time import sleep
jogos = []
numeros = []
countn = 0
countj = 0
print('=== GERADOR DE JOGOS MEGA-SENA ===')
escolha = int(input('Quantos jogos você deseja gerar? '))

while countj < escolha:
    while True:
        aleatorio = randint(1, 60)
        if aleatorio not in numeros:
            numeros.append(aleatorio)
            countn += 1
        if countn >= 6:
            break
    countn = 0
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    countj += 1

for l in range (0, escolha):
    print('=' * 25)
    print(jogos[l])
    #sleep(1)
print('=' * 25)
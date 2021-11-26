import random

n = int(input('Chute um número entre 1 e 10: '))
r = random.randint(1,10)
contador = 1
while n != r:
    n = int(input('Você errou. Tente mais uma vez. Chute um número de 1 a 10: '))
    contador += 1
print(f'Parabéns, você acrestou. O número sorteado pelo computador foi {r}. Você precisou de {contador} tentativas para acertar.')
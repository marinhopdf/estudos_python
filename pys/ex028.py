import random

n = int(input('Chute um número entre 1 e 5: '))
r = random.randint(1,5)
print(f'O número sorteado pelo computador foi {r}.')
if n == r:
    print('Você acertou o número.')
else:
    print('Você errou o número.')
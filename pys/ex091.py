from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
for k, v in jogo.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)
rank = {}
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rank)
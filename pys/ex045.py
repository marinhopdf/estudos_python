from random import randint

entrada = int(input('Escolha pedra, papel ou tesoura (1, 2 ou 3, respectivamente): '))

randcomputador = randint(1, 3)

if entrada == 1:
    jogador = 'pedra'
elif entrada == 2:
    jogador = 'papel'
elif entrada == 3:
    jogador = 'tesoura1'

if randcomputador == 1:
    computador = 'pedra'
if randcomputador == 2:
    computador = 'papel'
if randcomputador == 3:
    computador = 'tesoura'

print(f'Você jogou {jogador}. O computador jogou {computador}.')

if entrada == 1:
    if randcomputador == 1:
        print('Empate.')
    elif randcomputador == 2:
        print('O computador venceu.')
    elif randcomputador == 3:
        print('O computador perdeu.')
elif entrada == 2:
   if randcomputador == 2:
       print('Empate.')
   elif randcomputador == 3:
       print('O computador venceu.')
   elif randcomputador == 1:
       print('O computador perdeu.')
elif entrada == 3:
    if randcomputador == 3:
        print('Empate.')
    elif randcomputador == 1:
        print('O computador venceu.')
    elif randcomputador == 2:
        print('O computador perdeu.')
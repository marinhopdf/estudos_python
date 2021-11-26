info_jogador = {}
gols = []
info_jogador['nome'] = input('Digite o nome do jogador: ')
info_jogador['n_partidas'] = int(input('Digite quantas partidas ele jogou: '))
if info_jogador['n_partidas'] > 0:
    partidas = info_jogador['n_partidas']
    gols = [None]*partidas
    for i in range (0, partidas):
        gols[i] = int(input(f'Quantos gols foram feitos na partida {i+1}: '))
    info_jogador['gols'] = gols
print(info_jogador)

print(f'O jogador {info_jogador["nome"]} jogou {info_jogador["n_partidas"]} durante o campeonato e fez {sum(gols)} sendo a distribuição respectiva {gols}.')
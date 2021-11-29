def ficha(nome='', gols=''):
    if not nome:
        nome = '<desconhecido>'
    if not gols:
        gols = '0'

    return nome, gols


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite quantos gols o jogador fez: '))

print(f'O jogador {nome if nome else "<desconhecido>"} fez {gols if gols else "0"} gols.')

nome, gols = ficha(nome, gols)

print(f'O jogador {nome} fez {gols} gols.')

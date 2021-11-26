import random
c = 0
while True:
    e = str(input('Par ou ímpar (P ou I): ').upper().strip())[0]
    if e == 'I' or e == 'P':
        n = int(input('Digite o número: '))
        if n < 0:
            break
        npc = random.randint(0, 10)
        print(f'O computador jogou {npc}')
        soma = n+npc
        if soma%2 == 0:
            resultado = 'P'
        else:
            resultado = 'I'
        if resultado == e:
            print('Parábens, você venceu!')
            c += 1
        else:
            print(f'Você perdeu e acertou {c} vezes consecutivas.')
            c = 0
    else:
        print('Entrada inválida.')

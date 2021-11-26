while True:
    n = int(input('Digite o número ao qual deseja saber a tabuada: '))
    if n < 0:
        print('Entrada inválida.')
        break
    print('='*20)
    print(f'Tábuada do {n}')
    print('=' * 20)
    print('')
    for i in range (1,11):
        print(f'{n} x {i} = {n*i}')
    print('')
print('Programa encerrado.')

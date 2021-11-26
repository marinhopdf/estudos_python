tupla = ('Queijo', 20, 'Café', 5, 'Arroz', 7, 'Carne', 45, 'Pão', 6)
for posi in range (0, len(tupla)):
    if posi%2==0:
        print(f'{tupla[posi]:.<30}',end='')
    else:
        print(f'R${tupla[posi]:>3}')

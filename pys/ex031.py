d = float(input('Qual a distânci do destino? '))
if d <= 200:
    print(f'O preço da passagem será R$ {d*0.5}')
elif d > 200:
    print(f'O preço da passagem será R${d*0.45}')
else:
    print('Entrada invalida.')

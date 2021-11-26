v = float(input('Velocidade registrada: '))
if v > 50:
    print(f'Limite de velocidade ultrapassado!'
          f'\tA multra corresponde a R$ {(v-50)*7}')
else:
    print('Veículo dentro do limite de velocidade.')

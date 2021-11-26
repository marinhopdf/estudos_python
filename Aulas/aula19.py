pessoas = {'nome': 'Patrick','idade': '26', 'sexo': 'masculino'}
print(pessoas['nome'])
print(pessoas.keys())
print(pessoas.items())
print(f'O {pessoas["nome"]} é do sexo {pessoas["sexo"]} e tem {pessoas["idade"]} anos.')
print()
print('As chaves são: ')
for k in pessoas:
    print(k)

print()
print('Os valores das chaves são: ')
for v in pessoas.values():
    print(v)
del pessoas['sexo']
print()
print('As chaves e seus respectivos valores são: ')
for k, v in pessoas.items():
    print(f'{k} = {v}')
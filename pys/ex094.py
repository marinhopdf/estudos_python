flag = 'S'
cidadao = {}
pessoas = []
idade = media_idade = 0
mulheres = []
while True:
    cidadao['nome'] = input('Digite o nome do cidadão: ')
    cidadao['idade'] = int(input('Digite a idade do cidadão: '))
    idade += cidadao['idade']
    cidadao['sexo'] = str(input('Digite o sexo do cidadão (F ou M): ').upper().strip())[0]
    if (cidadao['sexo'] != 'F' and cidadao['sexo'] != 'M'):
        cidadao['sexo'] = (input('Por favor, digite somente F ou M: ').upper().strip())[0]
    pessoas.append(cidadao.copy())
    cidadao.clear()
    flag = str(input('Deseja continuar (S ou N)? ').upper().strip())[0]
    if flag != 'N' and flag != 'S':
        print('Por favor, digite somente S ou N: ')
    if flag == 'N':
        break
print('=-'*30)
print(f'O grupo tem {len(pessoas)} pessoas.')
media_idade = idade/len(pessoas)
print(f'A média da idade é {media_idade} anos.')

print(f'A(s) mulhere(s) do grupo: ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}')
print('A lista das pessoas acima da idade:')
for p in pessoas:
    if p['idade'] > media_idade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}',end = ' ')
        print()
print('>>> ENCERRADO <<<')
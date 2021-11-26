cm = 0
cf = 0
maiores = 0
mulheres20 = 0

while True:
    s = str(input('Digite o sexo do usuário (F ou M): ').upper().strip())[0]
    if s == 'M' or s == 'F':
        if s == 'M':
            cm += 1
        else:
            cf += 1
        idade = int(input('Digite a idade do usuário: '))
        if idade >= 18:
            maiores += 1
        if idade >= 20 and s == 'F':
            mulheres20 += 1
    else:
        print('Entrada inválida.')
    flag = str(input('Você deseja cadastrar mais usuários (S ou N)? ').upper().strip())[0]
    if flag == 'S':
        print('Insira a próxima pessoa no banco de dados.')
    else:
        break

print(f'Foram inseridos {maiores} pessoas maiores de idade no banco de dados.')
print(f'Dessas, {mulheres20} são mulheres com 20 anos ou mais.')
print(f'E um total de {cm} homens.')
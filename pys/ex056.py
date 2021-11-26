nome = [None]*4
idade = [None]*4
sexo = [None]*4

for i in range (0, 4):
    nome[i] = str(input(f'Digite o nome da pessoa {i+1}: '))
    idade[i] = int(input(f'Digite a idade da pessoa {i+1}: '))
    sexo[i] = str(input(f'Digite o sexo da pessoa (M ou F) {i+1}: '))

media = sum(idade)/len(idade)
print(f'A média de idade das pessoas é {media}.')

hmaisvelho = [None]*2
for n in range (1, 4):
    if sexo[n] == 'M' or sexo[n] == 'm':
        hmaisvelho = [nome[n], idade[n]]
        if idade[n] > hmaisvelho[1]:
            hmaisvelho = [nome[n], idade[n]]
print(f'O nome do homem mais velho é {hmaisvelho[0]}, com {hmaisvelho[1]} anos.')

fm = 0
for i in range (0, 4):
    if (sexo[i] == 'F' or sexo[i] == 'f') and (idade[i] <= 20):
        fm += 1

print(f'Existe(m) {fm} mulher(s) com 20 anos ou menos.')

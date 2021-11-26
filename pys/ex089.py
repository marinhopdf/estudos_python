boletins = []
alunos = ''
notas = []
media = 0
count = 0
while True:
    alunos = str(input('Digite o nome do aluno: '))
    notas.append(float(input('Digite a nota da primeira unidade: ')))
    notas.append(float(input('Digite a nota da segunda unidade: ')))
    media = sum(notas)/2
    boletins.append([alunos, notas[:], media])
    alunos = ''
    notas.clear()
    media = 0
    count += 1
    flag = str(input('Deseja continuar? [S/N]').upper().strip()[0])
    if flag == 'N':
        break
print(f'{"Nº":<4}| {"Nome":<10}|{"Média":>8}')
for i, a in enumerate (boletins):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*35)
    opc = int(input('Mostrar notas de qual aluno? [999 encerra]'))
    if opc == '99':
        break
    if opc <= len(boletins) -1:
        print(f'Notas de {boletins[opc][0]} são {boletins[opc][1]}')
print('Volte sempre.')
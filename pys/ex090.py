nome = str(input('Digite o nome do aluno: '))
nota = float(input(f'Digite a nota de {nome}: '))
aluno = {'nome': nome, 'media': nota}
situacao = ''
if aluno['media'] >= 7:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'
print(f'O aluno {aluno["nome"]} possui média {aluno["media"]} e está {situacao}.')

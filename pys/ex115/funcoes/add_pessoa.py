import csv

def adicionar():
    # nome = input('Digite o nome e sobrenome da pessoa: ')
    # idade = int(input('Digite a idade da pessoa: '))

    nome = 'teste_nome'
    idade = 18
    pessoas = {'Nome': nome, 'Idade': idade}
    header = ['Nome','Idade']
    dados = [pessoas['Nome'],pessoas['Idade']]

    with open('dados.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))












    # with open('dados.csv', 'a+', newline='') as csvfile:
    #     leitor = csv.reader(csvfile)
    #     writer = csv.writer(csvfile)
    #     if leitor.line_num < 1:
    #         writer.writerow(header)
    #     writer.writerow(dados)
    # with open('dados.csv', 'a+', encoding='UTF8', newline='') as f:


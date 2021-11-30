import time
from lib.interface import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        break
    else:
        print('ERRO! Digite um opção válida.')
    time.sleep(1)
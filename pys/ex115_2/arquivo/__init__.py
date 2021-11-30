from pys.ex115_2.lib.interface import cabeçalho

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('Pessoas encontradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
            a.close()

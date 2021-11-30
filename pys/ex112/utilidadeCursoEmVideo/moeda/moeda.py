def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + preco * (taxa / 100)
    return res if formatado is False else moeda(preco)


def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - preco * (taxa / 100)
    return res if formatado is False else moeda(preco)


def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if formatado is False else moeda(preco)


def metade(preco=0, formatado=False):
    res = preco / 2
    return res if formatado is False else moeda(preco)


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(p, a, d):
    print(f'O preço em vez de {moeda(p)} a prazo passa a ser de {aumentar(p, a)}, ou seja taxa de de {a}%.')
    print(f'O preço em vez de {moeda(p)} a vista passa a ser de {diminuir(p, d)}.')
    print(f'O dobro do preço original {moeda(p)} é {dobro(p)}.')
    print(f'A metade do preço original {moeda(p)} é {metade(p)}.')


def checagem(msg):
    valido = False
    while not valido:
        n = input(msg)
        if n.isalpha():
            print('Entrada inválida. Digite apenas números.')
        else:
            if ',' in n:
                n = n.replace(',', '.')
            valido = True
            return float(n)

def aumentar(preco = 0, taxa = 0, formatado=False):
    res = preco + preco * (taxa/100)
    return res if formatado is False else moeda(preco)

def diminuir(preco = 0, taxa = 0, formatado=False):
    res = preco - preco * (taxa/100)
    return res if formatado is False else moeda(preco)


def dobro(preco = 0, formatado=False):
    res = preco * 2
    return res if formatado is False else moeda(preco)


def metade(preco = 0, formatado=False):
    res = preco / 2
    return res if formatado is False else moeda(preco)

def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.',',')

from pys.ex113 import leiaInt

def linha(tam=42):
    return '_' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c}. {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


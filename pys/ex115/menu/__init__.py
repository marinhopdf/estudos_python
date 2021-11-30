import time

from pys.ex115.funcoes.add_pessoa import adicionar
from pys.ex115.funcoes.mostrar_pessoas import mostrar

def opcoes():
    #while True:
    print('='*30)
    print('======= MENU PRINCIPAL =======')
    print('=' * 30)

    print('1. Ver pessoas cadastradas')
    print('2. Cadastrar nova pessoa')
    print('3. Sair do Sistema')

    try:
        #menu = int(input('Sua opção: '))
        menu = 2
        if menu == 1:
            mostrar()
        elif menu == 2:
            adicionar()
        elif menu == 3:
            print('Sistema encerrado.')
            #break
    except ValueError:
        print('Entrada inválida.')
        time.sleep(1)
        print()
    except TypeError:
        print('Entrada inválida.')
        time.sleep(1)
        print()
    else:
        print('Salvando dados',end='')
        # for i in range(0,4):
        #     print('.',end='')
        #     time.sleep(0.5)
        # print()
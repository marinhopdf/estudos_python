import time

while True:
    print('\033[1;42m\033[1;97m ='*15)
    print('\033[1;42m\033[1;97m Programa de Ajuda python')
    print('\033[1;42m\033[1;97m ='*15)

    entrada = input('\033[1;105mDigite a função que você deseja consultar: [0 para encerrar] ')
    if entrada == '0':
        break
    print(f'\033[1;104m Consultando "{entrada}"')
    time.sleep(0.5)
    print(f'\033[1;104m {entrada.__doc__}')
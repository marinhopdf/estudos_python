def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
            break
        except:
            print('ERRO! Digite um valor numérico!')
    return entrada





def leiaInt(entrada):
    if entrada.isdigit():
        print(f'Você digitou o número {entrada}.')
        return False
    else:
        print('ERRO! Digite um valor numérico!')
        return True

parada = True

while parada:
    entrada = input('Digite um valor inteiro: ')
    parada = leiaInt(entrada)

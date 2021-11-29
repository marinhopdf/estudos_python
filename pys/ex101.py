from datetime import datetime

def voto(ano):
    data = datetime.now()
    data = data.year
    idade = data - ano
    if idade < 16:
        print('Voto negado:')
    elif idade < 18 or idade > 60:
        print('Voto opcional.')
    else:
        print('Voto obrigatório.')

nascimento = int(input('Digite seu ano de nascimento: '))
voto(nascimento)

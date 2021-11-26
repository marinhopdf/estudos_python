flag = 'S'
nome = ''
carteira_t = ''
ano_contratacao = 0
salario = 0
aposentadoria = 0
idade = 0
infos = {'Nome': nome, 'Idade': idade,'CTPS': carteira_t, 'Ano de contratação': ano_contratacao,
         'Salário': salario, 'Ano de aposentadoria': aposentadoria}
while True:
    infos['Nome'] = input('Digite o nome completo do trabalhador: ')
    infos['Idade'] = int(input('Insira o ano de nascimento do tabalhador: '))
    infos['Idade'] = 2021 - infos['Idade']
    infos['CTPS'] = input('Insira o número da inscrição da Carteira de Trabalho (0 para caso não exista) : ')
    if carteira_t != '0':
        infos['Ano de contratação'] = int(input('Por favor, o ano de contração: '))
        infos['Salário'] = input('Por favor, digite o salário: ')
        infos['Ano de aposentadoria'] = 35 + infos['Idade']
    else:
        infos['Ano de contratação'] = 0
        infos['Salário'] = 0
        infos['Ano de aposentadoria'] = 0
    if carteira_t != '0':
        print(f'{infos["Nome"]} tem {infos["Idade"]} anos, a carteira de trabalho é {infos["CTPS"]}.' )
        print(f'Foi contratado no ano {infos["Ano de contratação"]}.')
        print(f'Atualmente possui o salário de R$ {infos["Salário"]}.')
        print(f'E se aposentará com {infos["Ano de aposentadoria"]} anos.')
    else:
        print(f'{infos["Nome"]} tem {infos["Idade"]} anos.' )
    print()
    print()
    flag = str(input('Deseja continuar? [S ou N]').strip().upper)[0]
    if flag == 'N':

        break
    infos.clear()
    print()
    print()
print()
print()
print('Programa encerrado.')

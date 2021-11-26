preco = float(input('Digite o valor do produtor: '))
forma = int(input('Informe a forma de pagamento (1- à vista ou cheque. 2- débito. 3- em até 2x no cartão de crédito. 4- 3x ou mais no cartão de crédito): '))

if forma == 1:
    print(f'O valor pago no produtor será de R$ {preco*0.90}.')
elif forma == 2:
    print(f'O valor pago no produto será de R$ {preco*0.95}.')
elif forma == 3:
    parcelas = int(input('Deseja parcelar em quantas vezes?'))
    if parcelas < 3:
        print(f'O valor pago no produto será o preço integral de R$ {preco}, em duas parcelas de {preco/parcelas}')
    elif parcelas >= 3:
        print(f'O valor pago no produto será acrescido de 20% para cobrir o juros do cartão. O preço passará a ser de {preco * 1.2}, em {parcelas} parcelas de {(preco * 1.2) / parcelas}')
else:
    print('Entrada inválida.')
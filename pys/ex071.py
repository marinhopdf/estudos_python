while True:
    resto1 = 0
    resto10 = 0
    resto20 = 0
    resto50 = 0

    valor = int(input('Qual valor deseja sacar? '))
    valor2 = valor

    resto50 = valor2//50
    valor2 = valor2-resto50*50

    resto20 = valor2//20
    valor2 = valor2 - resto20 * 20

    resto10 = valor2 // 10
    valor2 = valor2 - resto10 * 10

    resto1 = valor2 // 1

    print(f'O valor de R$ {valor} será sacado em: ')
    if resto50 != 0:
        print(f'{resto50} cédulas de R$ 50,00.')
    if resto20 != 0:
        print(f'{resto20} cédulas de R$ 20,00.')
    if resto10 != 0:
        print(f'{resto10} cédulas de R$ 10,00.')
    if resto1 != 0:
        print(f'{resto1} cédulas de R$ 1,00.')
    break




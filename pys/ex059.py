menu = '4'
n1 = None
n2 = None
menu2 = None
while menu != '5':
    while menu == '4':
        n1 = float(input('Digite o primeiro novo número: '))
        n2 = float(input('Digite o segundo novo número: '))
        print ('Qual o próximo procedimento?')
        print ('[1] Somar')
        print ('[2] Multiplicar')
        print ('[3] Identidicar o maior número')
        print ('[4] Inserir novos números')
        print ('[5] Encerrar o programa')
        menu2 = str(input('Escolha uma das opções acima: '))
        if menu2 == '1':
            print (f'A soma dos números {n1} e {n2} é {n1+n2}.')
            menu2 = None
        elif menu2 == '2':
            print(f'A multiplicação dos números {n1} e {n2} é {n1*n2}.')
            menu2 = None
        elif menu2 == '3':
            if n1 > n2:
                print(f'O maior número é {n1}.')
                menu2 = None
            else:
                print(f'O maior número é {n2}.')
                menu2 = None
        elif menu2 == '4':
            menu2 = None
        elif menu2 == '5':
            menu = '5'
print('Programa encerrado.')
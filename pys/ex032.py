ano = int(input('Digite um ano: '))

if (ano%4 == 0) and (ano%100 != 0) or (ano%400==0):
    print('O ano É bissexto.')
else:
    print('O ano NÃO é bissexto.')

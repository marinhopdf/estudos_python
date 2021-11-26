expressao = str(input('Digite sua expressão matemática: '))
pa = expressao.count('(')
pf = expressao.count(')')
ppf = 0
tipoerro = ''
validade = True
if pa == pf:
    for element in expressao:
        if element == ')' and ppf==0:
            validade = False
            tipoerro = 'você fechou parenteses antes de abrir'
        elif element == '(':
            ppf += 1
        elif element == ')':
            ppf -= 1
else:
    validade = False
    tipoerro = 'o número de parenteses que abrem e fecham difere'

if validade == True:
    print('Expressão válida.')
else:
    print(f'Experessão inválida porque {tipoerro}.')

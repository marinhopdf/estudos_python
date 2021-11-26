n = str(input('Digete seu nome completo: ')).strip()
nn = (len(n) - n.count(' '))
nM = n.upper()
nm = n.lower()

print(f'O número de caracteres do seu nome é: {nn}')
print(f'Em letras maiúsculas fica assim: {nM}')
print(f'Em letras minúsculas fica assim: {nm}')
print('O primeiro nome possue {} letras' .format(n.find(' ')))

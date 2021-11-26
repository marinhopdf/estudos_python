inteiro = int(input('Digite um número inteiro: '))
print('Digite qual a base que deseja converter esse número: \n {1} Binário \n {2} Octal \n {3} Hexadecimal')
flag = int(input())

if flag == 1:
    print(f'{inteiro} em binário é {bin(inteiro)}')
elif flag == 2:
    print(f'{inteiro} em octal é {oct(inteiro)}')
elif flag == 3:
    print(f'{inteiro} em hexadecimal é {hex(inteiro)}')
else:
    print('Opção inválida.')

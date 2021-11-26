a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if ((b-c)<a<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
    print('Essas retas são capazes de formar um triângulo!')
else:
    print('Essas retas NÃO são capazes de formar um triângulo!')
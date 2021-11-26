import math

a = float(input('Digite o cateto adjacente: '))
b = float(input('Digite o cateto oposto: '))
print('A hipotenusa de um triangulo retângulo com essas características corresponde a {}.' .format(math.sqrt(math.pow(a,2)+math.pow(b,2))))

from math import factorial

def fatorial(numero, show=False):
    fatorial = factorial(numero)
    if show == True:
        print(fatorial)

n = int(input('Digite o número a ser descoberto o fatorial: '))
c = bool(input('Você deseja ver o valor? [0 para não ver | 1 para ver]'))

print(c)
print(type(c))

if c:
    fatorial(n, c)
else:
    fatorial(n)




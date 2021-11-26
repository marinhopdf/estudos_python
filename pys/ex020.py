import random

n1 = input('Digite o nome dos integrantes do grupos: ' )
n2 = input('Segundo: ')
n3 = input('Terceiro: ')
n4 = input('Quarto: ')
integrantes = [n1, n2, n3, n4]
random.shuffle(integrantes)
print(f'A ordem de apresentação será: {integrantes}')

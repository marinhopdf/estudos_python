x = 1
n1 = float(input(f'Digite o número {x} número: '))
x += 1
n2 = float(input(f'Digite o número {x} número: '))
x += 1
n3 = float(input(f'Digite o número {x} número: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
elif n2 < maior:
    menor = n2
if n3 > maior:
    m = n3
elif n3 < menor:
    menor = n3

print(f'O maior número foi {maior} e o menor foi {menor}' )

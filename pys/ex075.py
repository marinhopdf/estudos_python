n0 = int(input('Digite o númer 1: '))
n1 = int(input('Digite o númer 2: '))
n2 = int(input('Digite o númer 3: '))
n3 = int(input('Digite o númer 4: '))
n = (n0, n1, n2, n3)

nove = n.count(9)
print(f'O número 9 apareceu {nove} vez(es).')

tres = n.index(3)
print(f'O número 3 foi apareceu pela primeira vez na posição {tres+1}')

print(f'O(s) número(s) par(es) é(são): ')
for element in n:
    if element%2 == 0:
        print(f'{element}')
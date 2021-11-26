n = int(input('Digite o número ao qual deseja saber o fatorial: '))
count = n
fatorial = 1
while count > 0:
    fatorial *= count
    count -= 1
print(f'O fatorial de {n} é {fatorial}')
import uteis

def fatorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f



num=int(input('Digite o número que deseja saber o fatorial: '))
fat = fatorial(num)
double = uteis.dobro(num)
print(f'O fatorial de {num} é {fat} e seu dobro é {double}.')

print('='*20)
print('Sequência Fibonacci')
print('='*20)

n = int(input('Digite quantos termos gostaria de ver da sequência Fibonacci: '))
c = 0
f1 = 0
f2 = 1
while c <= n:
    f3 = f1 + f2
    print(f'\n{f3}')
    f1 = f2
    f2 = f3
    c += 1
print('Programa encerrado.')
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
t = int(input('Quanto termos você quer que o programa mostre? '))
pa=a1
i = 0
print(f'O termo {i+1} da PA é {pa} ')
while i != t:
    pa = pa + r
    print(f'O termo {i+1} da PA é {pa} ')
    i += 1
print('Programa encerrado.')
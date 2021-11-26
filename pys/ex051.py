a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
pa=a1
for i in range (1, 10):
    pa = pa + r
    print(f'O termo {i+1} da PA é {pa} ')
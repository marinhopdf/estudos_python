a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
pa=a1
i = 1
print(f'O termo {i} da PA é {pa} ')
while i < 10:
    pa = pa + r
    print(f'O termo {i+1} da PA é {pa} ')
    i += 1
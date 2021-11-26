times = ('Atlético-MG','Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians', 'Fortaleza', 'Internacional', 'Fluminense', 'América-MG',
         'Ceará', 'Athletico-PR', 'Santos', 'Cuiabá',
         'Atlético-GO', 'São Paulo', 'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense')

print('Os cinco primeiros colocados são: ')
print(times[0:5])

print('\nOs quatro últimos colocados são: ')
print(times[-4:])

print('\nOs times da série A são: ')
for element in times:
    print(element)
chape = times.index("Chapecoense")+1
print(f'A posição do Chapecoense é {chape}')

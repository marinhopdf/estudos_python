from datetime import date

ano = [None] * 6
atual = date.today().year
maiores = 0
menores = 0
for i in range(0, 6):
    ano[i]=int(input(f'Digite o ano de nascimento da pessoa {i+1}: '))
    if ano[i] > 2003:
        menores += 1
    else:
        maiores += 1
print(f'{maiores} pessoas são maiores de idade.')
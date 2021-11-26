idade = int(input('Digite a idade do atleta nadador: '))

if idade < 10:
    print('Atleta competirá na categoria mirim.')
if idade < 15 and idade >= 10:
    print('Atleta competirá na categoria infantil.')
if idade < 20 and idade >= 15:
    print('Atleta competirá na categoria júnior.')
if idade < 21 and idade >= 20:
    print('Atleta competirá na categoria sênior.')
if idade >= 21:
    print('Atleta competirá na categoria master.')
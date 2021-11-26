nota1 = float(input('Digite a nota da primeira unidade: '))
nota2 = float(input('Digite a nota da segunda unidade: '))

media = (nota1+nota2)/2

if media >= 7:
    print('Aprovado.')
if media >= 5 and media <= 6.9:
    print('Recuperação.')
if media < 5:
    print('Reprovado.')
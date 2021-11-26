nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2021 - nascimento
refratario = idade - 18
anodealistamento = nascimento + 18
ano = 18 - idade
if idade > 18:
    print(f'Você está refratário faz {refratario} anos. Procure a junta de alismamento militar mais próxima para regularizar sua situação.')
elif idade < 18:
    print(f'Vocẽ deve se alistar até dezembro do ano {anodealistamento}. Faltam {ano} ano(s) para você se alistar. Procure a junta de alismamento militar mais próxima para regularizar sua situação.')

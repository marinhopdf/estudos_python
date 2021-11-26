salario = float(input('Qual o seu salário? '))
emprestimo = float(input('Qual o momante deseja tomar emprestado? '))
anos = int(input('Em quantos anos deseja pagar o empréstimo? '))
parcela = emprestimo/(anos*12)
print(f'Para pagar R$ {emprestimo} em {anos} anos a parcela será de {parcela}.')

condicao = parcela/salario
print(f'Condição: R$ {condicao}.')

if condicao > 0.3:
    print('Lamentamos, mas você não poderá tomar o empréstimo nessas condições.')
elif condicao < 0.3:
    print('Parabéns! Seu empréstimo foi pré-aprovado!')
else:
    print('!!! Erro no procedimento. !!!')

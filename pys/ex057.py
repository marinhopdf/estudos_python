sexo = str(input('Digite o gênero do usuário (M ou F): ').strip().upper())[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe o utilizando os parâmetros corretos').strip().upper()[0])
print(f'O gênero do usuário é {sexo}.')
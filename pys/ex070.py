maisque1k = 0
valortotal = 0
menorpreco = 0
continuar = 'S'

while True:
    if continuar == 'S':
        nome = str(input("Nome do produto: "))
        preco = float(input("Preço do produto: "))
        if menorpreco > preco or menorpreco == 0:
            menorpreco = preco
            maisbarato = nome
        if preco > 1000:
            maisque1k += 1
        valortotal = valortotal + preco
    continuar = str(input("Você deseja continuar(S ou N)?").upper().strip())[0]
    if continuar == 'N':
        break
    if continuar == 'S':
        print('Insira as informações do pŕoximo produto.')
    else:
        print('Entrada inválida. Por favor, insira os parâmetros corretos.')

print(f'O valor total da compra foi de R$ {valortotal}.')
print(f'Foram comprados {maisque1k} produto(s) por mais de R$ 1000,00.')
print(f'O nome do produto mais barato é {maisbarato}.')
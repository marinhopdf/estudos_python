p = float(input('Qual o preço do produto? '))
q = int(input('Qual a quantidade de produtos? '))

print('O valor da compra foi: R$ {:.2f} (5% de desconto)' .format((p*q)*0.95))

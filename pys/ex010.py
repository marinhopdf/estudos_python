d = float(input('Qual a cotação do dólar hoje? '))
r = float(input('Quantos reais você possui em sua carteira? '))

print ('Com a cotação atual do de {} você consegue comprar {:.2f} Dólares com {} Reais.' .format(d, r/d, r))

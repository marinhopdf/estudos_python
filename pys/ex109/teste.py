import moeda

p = float(input('Digite o preço do produto: '))
a = float(input('Quanto será o aumento à prazo: '))
d = float(input('Quanto será o desconto à vista: '))

print(f'O preço em vez de {moeda.moeda(p)} a prazo passa a ser de {moeda.aumentar(p,a,True)}, ou seja taxa de de {a}%.')
print(f'O preço em vez de {moeda.moeda(p)} a vista passa a ser de {moeda.diminuir(p,d)}.')
print(f'O dobro do preço original {moeda.moeda(p)}  é {moeda.dobro(p, True)}.')
print(f'A metade do preço original {moeda.moeda(p)} é {moeda.metade(p)}.')






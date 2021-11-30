from ex108 import moeda

p = float(input('Digite o preço do produto: '))
a = float(input('Quanto será o aumento à prazo: '))
d = float(input('Quanto será o desconto à vista: '))

print(f'O preço em vez de {moeda.moeda(p)} a prazo passa a ser de {moeda.moeda(moeda.aumentar(p,a))}, ou seja taxa de de {a}%.')
print(f'O preço em vez de {moeda.moeda(p)} a vista passa a ser de {moeda.moeda(moeda.diminuir(p,d))}.')
print(f'O dobro do preço original {moeda.moeda(p)}  é {moeda.moeda(moeda.dobro(p))}.')
print(f'A metade do preço original {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')






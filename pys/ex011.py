h = float(input('Qual a altura da parade?'))
l = float(input('Qual a largura da parade?'))
a = h*l
print('Considerando que 1 litro de tinta pinta 2 m² de parede, você necessitará de {:.2f} litro(s) de tinta para pintar sua parede, que possui uma área correspondente de {:.2f}' .format((a/2),a))

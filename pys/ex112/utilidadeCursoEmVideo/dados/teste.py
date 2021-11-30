from pys.ex112.utilidadeCursoEmVideo.moeda import moeda

preco = moeda.checagem('Digite o preço do produto: ')
aumento = moeda.checagem('Quanto será o aumento à prazo: ')
desconto = moeda.checagem('Quanto será o desconto à vista: ')

moeda.resumo(preco, aumento, desconto)





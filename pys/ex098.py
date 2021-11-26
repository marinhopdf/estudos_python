#import time
#
# def contador(inicio, fim, passo):
#     lista = []
#     lista.append(inicio)
#     if passo == 0:
#         passo = 1
#     if fim > inicio:
#         i = 1
#         while fim not in lista or lista:
#             elemento = lista[i-1] + passo
#             lista.append(elemento)
#             i += 1
#     else:
#         i = 1
#         while fim not in lista:
#             elemento = lista[i - 1] - passo
#             lista.append(elemento)
#             i += 1
#
#     print('Contagem: ', end=' ')
#     for i in range (0, len(lista)):
#         print(f'{lista[i]},', end=' ')
#         #time.sleep(1)
#
#
# n1 = int(input('Digite o valor inicial da contagem: '))
# n2 = int(input('Digite o valor final da contagem: '))
# n3 = int(input('Digite o espaçamento da contagem: '))
# contador(n1, n2, n3)

def contador(inicio, fim, passo):
    range(inicio, fim, passo)
    lista = list(range(inicio, fim, passo))

    print('Os elemento do contagem são: ',end=' ')
    for i in lista:
        print(f'{i}, ',end=' ')
        #time.sleep(1)


n1 = int(input('Digite o valor inicial da contagem: '))
n2 = int(input('Digite o valor final da contagem: '))
n3 = int(input('Digite o espaçamento da contagem: '))

contador(n1, n2, n3)

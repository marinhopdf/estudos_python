def escreva(texto):
    tamanho = len(texto)
    print('~'*tamanho)
    print(texto)
    print('~'*tamanho)

entrada = input('Escreva a mensagem: ')
escreva(entrada)
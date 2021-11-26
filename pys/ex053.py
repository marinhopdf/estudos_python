frase = str(input('Digite uma frase para verificar se ele é um palíndromo: ')).strip().upper()
print(f'Você digitou a frase "{frase}"')

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso da frase é "{inverso}".')

if inverso == junto:
    print('Você digitou uma frase palíndroma.')
else:
    print('A fase digitada não é um palíndromo.')

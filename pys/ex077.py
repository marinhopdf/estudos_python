palavra = (str(input('Digete uma palavra: ')),
           str(input('Digete uma palavra: ')),
           str(input('Digete uma palavra: ')),
           str(input('Digete uma palavra: ')),
            str(input('Digete uma palavra: ')),
           )
for element in palavra:
    print(f'\nNa palavra "{element}" temos: ', end='')
    for letra in element:
        if letra.lower() in 'aeiou':
            print(f'"{letra}"', end=' ')
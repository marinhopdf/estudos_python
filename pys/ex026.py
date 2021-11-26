p = str(input('Digite uma palavra: ')).strip()
p = p.lower()
pl = p.find('a') + 1
ul = p.rfind('a') + 1
print('A letra \'a\' aparece {} vezes' .format(p.count('a')))
print(f'A primeira vez foi como letra {pl}')
if p.count('a') > 1 :
    print(f'A última vez foi como letra {ul}')

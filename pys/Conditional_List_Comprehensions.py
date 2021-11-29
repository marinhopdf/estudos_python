alfa = 'abcdefghijklmnopqrstuvwxyz'
vogais = 'aeiou'

a = [x.upper() for x in alfa]
b = []
c = []
d = [x for x in alfa if x in vogais]


for x in alfa:
    if x in vogais:
        b.append(x)
        c.append(x.upper())

print(a)
print(b)
print(c)
print(d)
print([x**2 for x in [2, 3, 5]])
print([x if x%2 == 0 else x+1 for x in [2, 3, 4, 5, 7, 9]])
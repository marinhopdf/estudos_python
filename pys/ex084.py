temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(float(input('Digite o peso da pessoa: ')))
    if len(temp) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    flag = str(input('Você deseja continuar? [S/N]').upper().strip())
    if flag == 'N':
        break

print(f'Os dados cadastrados foram {princ}.')
print(f'O número de pessoas cadastradas foi {len(princ)}')
print(f'O maior peso foi de {mai} e o menor foi de {men}.')
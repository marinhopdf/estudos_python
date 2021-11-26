s = float(input('Digite o salário do funcionário: '))

if s > 1250:
    sn = s*1.10
elif s <= 1250:
    sn = s*1.15
print(f'O novo salário do funcionário corresponderá a R$ {sn}.')

pesos = [None]*5
for i in range (0, 5):
    pesos[i] = int(input(f'Digite o peso da pessoa {i+1}: '))
print(f'A pessoa de maior peso possui {max(pesos)} e a de menor peso possui {min(pesos)}.')
import csv

def mostrar():
    with open('./dados.csv', 'a+', newline='') as csvfile:
        leitor = csv.reader(csvfile)
        for row in leitor:
            print(', '.join(row))
            reader = csv.reader(csvfile)




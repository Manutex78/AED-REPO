def aboveAverage(numeros):
    total = sum(numeros)
    media = total / 10
    print(media)
    counter = 0  # Initialize counter
    for i in range(10):
        if numeros[i] > media:
            counter += 1
    return "{:n} dos números inseridos estão acima da média".format(counter)

numeros = []  # Initialize empty list
for i in range(10):
    numero = int(input("Introduza um valor: "))
    numeros.append(numero)  # Append values to the list

print(aboveAverage(numeros))

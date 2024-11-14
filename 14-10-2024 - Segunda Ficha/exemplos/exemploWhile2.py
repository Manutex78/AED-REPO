# Exemplos de estruturas repetivivas / Iterativas - ciclo while

numero=int(input("Indique um número entre [0-20]: "))

while numero <= 0 or numero >20:
    print("Indicou um numero inválido. Tente novamente! \n")
    numero=int(input("Indique um número entre [0-20]: "))
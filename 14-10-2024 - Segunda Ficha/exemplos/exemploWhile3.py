# Exemplos de estruturas repetivivas / Iterativas - ciclo while

tabuada=int(input("Imprimir a tabuada dos: "))
numero=1

while numero<11:
    print("{:n} * {:n} = {:n}" .format(tabuada, numero, tabuada*numero))
    numero+=1
tabuada = int(input("Imprimir a tabuada do: "))
numero = 0
while numero<10 :
    numero+=1
    if numero ==6:
        continue
    print(tabuada,"*", numero, "=", tabuada*numero)
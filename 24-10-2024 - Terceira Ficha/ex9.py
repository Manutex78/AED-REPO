def printCharline(texto,numeroCar):
    
    nc = numeroCar
    for i in range(0,len(texto)):
        if i+1 == numeroCar:
            numeroCar+=nc
            print(texto[i]+"\n",end="")
        else:
            print(texto[i],end="")
        

texto = input("Texto: ")
numeroCar = int(input("Número de caracteres por linha: "))

printCharline(texto,numeroCar)
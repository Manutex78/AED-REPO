valido = False

def printCharline(texto,numeroCar):
    
    nc = numeroCar
    for i in range(0,len(texto)):
        if i+1 == numeroCar:
            numeroCar+=nc
            print(texto[i]+"\n",end="")
        else:
            print(texto[i],end="")


texto = input("Texto: ")

while not valido: 
    try:
        numeroCar = int(input("Número de caracteres por linha: "))
        if numeroCar >= 5 and numeroCar <= 12:
            print(printCharline(texto,numeroCar))
        else:
            raise ValueError()
    except ValueError:
        print("Insira um valor entre 5-12!")
    else:
        valido = True


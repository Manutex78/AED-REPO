

def maior(*numeros:int):

    maiorNumero = 0

    for i in range(len(numeros)):
        if numeros[i]>maiorNumero:
            maiorNumero = numeros[i]
    return maiorNumero



print(maior (10,20))
print(maior (10,30,20))
print(maior (5,15,20,14))
import math

def funcao(numeros):

    min = math.inf
    media = sum(numeros)/len(numeros)

    for i in range(len(numeros)):
        if abs(numeros[i]-media) < min:
            min = numeros[i]
    
    return min

print(funcao([5,10,20,12]))
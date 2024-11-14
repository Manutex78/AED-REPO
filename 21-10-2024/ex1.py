

def somatorio(n1,n2):

    soma=0

    if n2>n1:
        for i in range(n1,n2+1):
            soma+=i
        return soma
    elif n1>n2:
        for i in range(n1,n2-1,-1):
            soma+=i
        return soma
    else:
        return "Introduza 2 números diferentes"


n1=int(input("Introduza um numero: "))
n2=int(input("Introduza um numero: "))

print(somatorio(n1,n2))

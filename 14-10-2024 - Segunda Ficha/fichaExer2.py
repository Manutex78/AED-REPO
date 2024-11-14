soma=0
limInferior=int(input("Indique o limite inferior: "))
limSuperior=int(input("Indique o limite superior: "))
i=limInferior
for i in range(limSuperior+1):
    if i % 2 == 0:
        soma += i

print("A soma de todos os pares entre {:n} e {:n} é {:n}".format(limInferior,limSuperior,soma))
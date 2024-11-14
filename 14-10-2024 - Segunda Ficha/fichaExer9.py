
maior=0
segundoMaior=0

lerNum=int(input("Qts numeros deseja ler? ")) 

for i in range(lerNum):
    num = int(input("Número: "))

    if num > maior:
        segundoMaior = maior
        maior = num
    elif num > segundoMaior:
        segundoMaior = num
        

print("Maior Número: {:n}".format(maior))
print("Segundo Maior Número: {:n}".format(segundoMaior))



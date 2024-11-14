num = int(input("Número: "))
binario = str("")
if num <= 99 and num >=1:
    while num >= 1:
        #print(num % 2, end = " ")
        valor = num % 2
        binario = str(valor)+ " " + binario 
        num //= 2
    print(binario)
else:
    print("Introduza um número entre 1 e 99!")

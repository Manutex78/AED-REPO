numFibonacci = int(input("Nº de termos a imprimir: "))

if numFibonacci == 0:
    print("0")
elif numFibonacci ==1:
    print("0")
elif numFibonacci == 2:
    print("0,1")
else:
    a = 0
    b = 1
    nextNumber = a + b
    count = 3
    print(a, b, end=" ")
    while count <= numFibonacci:
        print(nextNumber, end=" ")
        a = b
        b = nextNumber
        nextNumber = a + b
        count += 1

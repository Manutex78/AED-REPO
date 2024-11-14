lista = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]]

print("----------")

for i in range(len(lista)):
    for j in range(len(lista[i])):
        for k in range(len(lista[i][j])):
            print(lista[i][j][k],end=" ")
        print()
    print()

import random

lista2 = []

for i in range(3):
    lista2.append([])
    for j in range(3):
        lista2[i].append([])
        for k in range(3):
           lista2[i][j].append(random.randint(0,30))

print("----------")

for i in range(len(lista2)):
    for j in range(len(lista2[i])):
        for k in range(len(lista2[i][j])):
            print(lista2[i][j][k],end=" ")
        print()
    print()

print("----------")

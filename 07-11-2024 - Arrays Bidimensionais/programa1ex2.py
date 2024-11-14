import random

matriz = []


def startMatriz(tamanho):
    if len(matriz) != 0:
        matriz.clear()
        for i in range(tamanho):
            matriz.append([])
            for j in range(tamanho):
                matriz[i].append(random.randint(10, 100))
    else:
        for i in range(tamanho):
            matriz.append([])
            for j in range(tamanho):
                matriz[i].append(random.randint(10, 100))
        
        print("Matriz Gerada: ")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=' ')
            print()
                
def matrizTrans():
    print("Matriz Original:\n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=" ")
        print()
    print("\n")
    
    print("Matriz Transposta:\n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[j][i],end=" ")
        print()

def maxValue():
    maior = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>maior:
                maior = matriz[i][j]
    return f"O maior valor da matriz é {maior}"

programa = False
while not programa:
    print("\n\t\tMENU")
    print("1 - Inicializar matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior Valor")
    print("0 - Sair")

    try:
        op = int(input("Escolha uma das opções: "))
        if op > 3 or op < 0:
            raise ValueError()
    except ValueError:
        print("Opção Inválida >:[")
    except:
        print("Erro")
    else:
        match op:
            case 1:
                tamanho = int(input("Digite o tamanho da matriz: "))
                startMatriz(tamanho)
            case 2:
                matrizTrans()
            case 3:
                print(maxValue())
            case 0:
                programa = True
                print("Adiós! :(")
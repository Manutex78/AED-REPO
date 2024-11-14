def searchNumber(valores,pesquisa):
    posicao = []
    ocor = valores.count(pesquisa)
    if ocor > 1:
        i = 0
        while i < ocor:
            pos1 =valores.index(pesquisa+i)
            posicao.append(pos1)

        return f"O valor {pesquisa} ocorre {ocor} vezes nas posições {posicao}"
    else:
        return valores.index(pesquisa)

valores = []
i = 1
while i <= 10:
    try:
        valor = int(input(f"Digite o valor {i}: "))
    except:
        print("Valor invalido, tente novamente")
    else:
        valores.append(valor)
        i+=1

pesquisa = int(input("Valor que deseja procurar: "))
print(searchNumber(valores,pesquisa))
        

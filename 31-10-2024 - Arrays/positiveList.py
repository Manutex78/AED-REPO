def positiveList(valores):
    for i in range(len(valores)):
        if valores[i] >= 10:
            pontFinal.append(valores[i])
    return f"Pontuações Positivas: {pontFinal}"



"""
Ler pontução de 10 participantes
"""
valores=[]
pontFinal = []
i = 1

while i <=  10:
    try:
        valor = int(input("Pontuação do {:n}º participante: ".format(i)))
        if valor < 0  or valor > 20:
            raise  ValueError()
    except ValueError:
        print("Pontuação fora do intervalo [0-20]")

    except:
        print("O valor introduzido não é válido")
    else:
        valores.append(valor)
        i+=1
print(positiveList(valores))


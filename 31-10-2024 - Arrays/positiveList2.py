def positiveList(valores,nomes):
    for i in range(len(valores)):
        if valores[i] >= 10:
            pontFinal.append(valores[i])
        else:
            del nomes[i]
    return f"Participantes com pontuações positivas\n\nNomes\t\t:{nomes}\nPontuações: {pontFinal}"

"""
Ler pontução de 10 participantes e os seus nomes
"""
nomes=[]
valores=[]
pontFinal = []
i = 1

while i <=  10:
    try:
        nome = str(input("Nome do {:n}º participante: ".format(i)))
        valor = int(input("Pontuação do {:n}º participante: ".format(i)))
        if valor < 0  or valor > 20:
            raise  ValueError()
        elif nome == "":
            raise NameError()
    except ValueError:
        print("Pontuação fora do intervalo [0-20]")
    except NameError:
        print("Nome não pode ser vazio")
    except:
        print("O valor introduzido não é válido")
    else:
        nomes.append(nome)
        valores.append(valor)
        i+=1
print(positiveList(valores,nomes))


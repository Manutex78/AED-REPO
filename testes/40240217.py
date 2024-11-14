#Manuel Teixeira 40240217
import math
"""
Programa que lê a temperatura ocorrida em cada uma das cidades de uma lista pré-definida. 
E no fim imprime o valor mais distante da média das temperaturas e a respetiva cidade
"""
cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

def dadosEstatistica(temperaturas):
    max = -math.inf
    media = sum(temperaturas)/len(temperaturas)

    for i in range(len(temperaturas)):
        if abs(temperaturas[i] - media) > max:
            max = temperaturas[i]
            cidade = cidades[i]

    return f"A temperatura mais distante da média é {max} que pertence a {cidade}!"


count = 0
temperaturas = []                                                                       #lista das temperaturas
while count < len(cidades):
    try:
        temperatura = int(input(f"Introduza um a temperatura em {cidades[count]}: "))   #Intodução da Temperatura
        if temperatura < 0 or temperatura > 40:                                         #Verifica se o valor introduzido está entre 0 e 40
            raise ValueError()                                                          #caso não esteja chama um erro
    except ValueError:
        print("Introduza um valor entre [0-40]!")
    except:
        print("Valor Inválido")
    else:
        temperaturas.append(temperatura)                                                #caso esteja adiciona o valor à lista
        count += 1

print(dadosEstatistica(temperaturas))
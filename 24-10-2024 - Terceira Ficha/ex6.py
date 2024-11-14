def standardName(nome):

    posPrimeiroEspaco = nome.find(" ")
    posUltimoEspaco = nome.rfind(" ")
    nomeStandard = nome[:posPrimeiroEspaco]

    for i in range(posPrimeiroEspaco,posUltimoEspaco):
        if nome[i] == " ":
            nomeStandard += " " + str(nome[i+1]) + "."

    nomeStandard += nome[posUltimoEspaco:]
    return nomeStandard

nome = input("Introduza o nome: ")
print(standardName(nome))
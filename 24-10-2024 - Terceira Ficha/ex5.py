def shortName(nome):
    posPrimeiroEspaco = nome.find(" ")
    posUltimoEspaco = nome.rfind(" ")

    return nome[:posPrimeiroEspaco] + nome[posUltimoEspaco:]

nome = input("Introduza o nome: ")
print(shortName(nome))
def removeSpaces(texto):
    return " ".join(texto.split())

texto = input("Indique um texto: ")
print(removeSpaces(texto))
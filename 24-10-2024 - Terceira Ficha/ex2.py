def countText(texto):

    vogais="aeiouAEIOU"
    numVogais = sum(texto.count(vogal) for vogal in vogais)
    numEspacos = texto.count(" ")

    print("Nº de Caracteres: {:n}\nNº de vogais: {:n}\nNº de espaços: {:n}".format(len(texto),numVogais,numEspacos))


texto = input("Indique um texto: ")
countText(texto)
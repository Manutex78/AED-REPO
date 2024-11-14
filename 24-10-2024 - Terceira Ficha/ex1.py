def invertText(texto):
   """ 
    comp = len(texto)
    for i in range(comp-1,-1,-1):
        print(texto[i], end="")
    """
   print(texto[::-1])

texto = input("Indique um texto: ")
invertText(texto)
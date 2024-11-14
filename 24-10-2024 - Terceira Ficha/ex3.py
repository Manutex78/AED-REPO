def capicua(texto):
    pCapicua = ""
    comp = len(texto)
    for i in range(0,comp):
        pCapicua = texto[i] + pCapicua
    
    if pCapicua == texto:
        return True
    else:
        return False


texto = input("Indique um texto: ")
if capicua(texto.lower()) == True:
    print("{:s} é uma capicua!".format(texto))
else:
    print("{:s} não é uma capicua!".format(texto))
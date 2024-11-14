def reverseWords(texto):

    a = texto.split()
    textoInvertido = a[::-1]
    return " ".join(textoInvertido)

texto = input("Texto: ")
print(reverseWords(texto))

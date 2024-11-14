"""

"""

genero = str(input("Indique o sexo(M/F): "))

altura = int(input("Indique a altura (cm): "))

match genero.upper():
    case "M":
        pesoIdeal=(altura-100) - (altura-150)/4
        print("O Peso Ideal é {:.2f} Kg".format(pesoIdeal))
    case "F":
        pesoIdeal=(altura-100) - (altura-150)/2
        print("O Peso Ideal é {:.2f} Kg".format(pesoIdeal))
    case _:
        print("Indique o sexo.")
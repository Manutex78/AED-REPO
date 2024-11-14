peso = float(input("Peso (kg): "))

altura = float(input("\nAltura (m): "))

IMC= peso/(altura**2)

print("O seu IMC é: {:.2f}".format(IMC))

if IMC < 18.25:
    print("\tBaixo Peso")
elif IMC < 25:
    print("\tPeso Normal")
elif IMC < 30:
    print("\tExcesso de Peso")
elif IMC <35:
    print("\tObesidade Grau I")
elif IMC <40:
    print("\tObesidade Grau II")
elif IMC >=40:
    print("\tObesidade Mórbida")
"""
CALCULA O IMC DA SEGUINTE FORMA:
PESO/(ALTURA^2)
"""
peso = float(input("Peso (kg): "))

altura = float(input("Altura (m): "))

IMC= peso/(altura**2)

print("O seu IMC é: {:.2f}.".format(IMC))
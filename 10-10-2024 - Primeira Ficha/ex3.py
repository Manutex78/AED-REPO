"""
CALCULA O PESO IDEAL DE UMA PESSOA ATRAVES 
DA ALTURA DA SEGUINTE FORMA: (altura-100)*0.9
"""


altura = int(input("Altura em cm: "))

pesoIdeal = (altura-100)*0.9

print("Peso ideal: {:.2f} Kg".format(pesoIdeal))
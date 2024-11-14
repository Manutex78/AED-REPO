"""
Simulador de peso noutros planetas, em função da sua gravidade relativa
"""


print("\t\t\t\t\tPlanetas")
print("\t\t\t\t1 - Mercúrio")
print("\t\t\t\t2 - Venus")
print("\t\t\t\t3 - Marte")
print("\t\t\t\t4 - Jupiter")
print("\t\t\t\t5 - Saturno")
print("\t\t\t\t6 - Urano")

peso = int(input("Indique o seu peso(kg): "))
planeta = int(input("Indique o código do planeta: "))

match planeta:
    case 1: gravidade=0.37
    case 2: gravidade=0.90
    case 3: gravidade=0.37
    case 4: gravidade=2.53
    case 5: gravidade=1.06
    case 6: gravidade=0.91
    case _:
        print("Escolha um planeta!")
pesoPlaneta = (peso * gravidade)/0.98
print("O seu peso de {:.2f} kg no planeta {:n} seria de {:.2f} Kg".format(peso,planeta,pesoPlaneta))
"""
CALCULA A FREQUENCIA CARDIACA MAXIMA DEPENDENO DO SEXO E DA IDADE
DA SEGUINTE FORMA: fcmHomens = 226 - idade E fcmMulheres = 220 - idade
"""

genero = str(input("\nIndique o Sexo (M/F):"))

idade = int(input("\nIndique a idade: "))

match genero.upper():
    case "M":
        fcm = 226 - idade
        print("FCM= {:n} bpm".format(fcm))
    case "F":
        fcm = 220 - idade
        print("FCM= {:n} bpm".format(fcm))
    case _:
        print("Indique o genero.")
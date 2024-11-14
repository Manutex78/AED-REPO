"""
CONVERTE O TEMPO EM SEGUNDOS PARA HORAS/MINUTOS/SEGUNDOS
"""

tempo = int(input("Indique o tempo em segundos: "))

horas = int(tempo/3600)
tempo -= (horas*3600)

minutos = int((tempo)/60)
tempo -= (minutos*60)

segundos = tempo

print("{:n} hora(s), {:n} minuto(s) e {:n} segundo(s).".format(horas,minutos,segundos))
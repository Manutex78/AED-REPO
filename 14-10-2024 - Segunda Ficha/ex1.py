"""
Programa que lê 10 números e no final indica a média e o maior inserido
"""
total=0
maior=0
i=0         #variavel que conta o numero de vezes que o ciclo foi executado

while i<10:
    numero = int(input("Indique o {:n}º número: ".format(i+1)))
    if numero > 20:
        continue
    if maior < numero:
        maior=numero
    total+=numero
    i+=1
media=total/10
print(f"A média é {media}")
print(f"O maior é {maior}")


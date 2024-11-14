"""
Calcula o fatorial do numero inserido
"""
numero = int(input("Introduza um número: "))
fatorial = numero
i = numero

if numero == 0:
    print("O fatorial de 0 é 1")
else:
    while i > 1:
        fatorial *= (i-1)
        i-=1
    print("O fatorial de {:n} é {:n}".format(numero,fatorial))
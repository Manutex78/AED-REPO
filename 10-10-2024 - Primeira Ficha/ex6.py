"""
VERIFICA SE O NÚMERO INTRODUZIDO É PAR OU IMPAR
"""
numero = int(input("Introduza um número inteiro: "))
if(numero % 2) == 0: 
    print("O número {:n} é par".format(numero))
    
else: 
    print("O número {:n} é impar".format(numero))
    
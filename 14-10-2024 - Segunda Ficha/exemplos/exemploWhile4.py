# Exemplos de estruturas repetivivas / Iterativas - ciclo while

import random # biblioteca que permite gerar números aleatoriamente

numeroGerado=random.randint(0,20) # gera um nº inteito entre 0 e 20
                                # inclui os limites inferior e superior
palpite = int(input("Indique o seu palpite:"))
tentativas = 1
while numeroGerado != palpite:
    print("Nao acertou! : ( tente novamente! \n")
    palpite = int(input("Indique o seu palpite:"))
    tentativas +=1
print(f"Acertou em {tentativas} tentativas")
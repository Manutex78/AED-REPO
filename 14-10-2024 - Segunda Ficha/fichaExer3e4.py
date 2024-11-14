import random
import os

def jogo(counter,guess,num):
    
    while guess != num and counter<10 :
        os.system("cls")
        counter+=1
        if guess > num:
            print("O número é MENOR\n")
        else:
            print("O número é MAIOR\n")

        guess = int(input("Indique o seu palpite: "))
            
    if counter >= 10:
        print("Esgotou as 10 tentativas :(")
    else:
        print("Parabéns! Acertou em {:n} tentativa(s)".format(counter))
        
    novoJogo=input("Novo Jogo(S/N)?: \n")
    
    match novoJogo.upper():

        case 'S':
            counter = 1
            guess = int(input("Indique o seu palpite: "))
            num = random.randint(1,50)
            jogo(counter,guess,num)
            
        case 'N':
            print("OK!")


counter = 1
num = random.randint(1,50)


print("\t\t\tJOGO Adivinha o Número\n")
guess = int(input("Indique o seu palpite: "))
jogo(counter,guess,num)



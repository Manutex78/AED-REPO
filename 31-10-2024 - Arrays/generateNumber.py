import random

def generateNumbers(limInf,limSup,quant):
        chaveEuro = []

        if quant == 5:
            while len(chaveEuro) != quant:
                chave = random.randint(limInf,limSup)
                if chave in chaveEuro:
                    continue
                else:
                    chaveEuro.append(chave)
            return f"Chave do Euromilhões: {chaveEuro}"
        
        if quant == 2:
            chaveEuro.clear()
            while len(chaveEuro) != 2:
                estrela = random.randint(limInf,limSup)
                if estrela in chaveEuro:
                    continue
                else:
                    chaveEuro.append(estrela)
            return f"Estrelas: {chaveEuro}"
        
        
    
print(generateNumbers(1,50,5)+"\t",end="")
print(generateNumbers(1,12,2)+"\n")
novoJogo = False

while not novoJogo:
    newGame = str(input("\nDeseja gerar uma nova chave (S/N): "))
    match newGame.upper():
        case "S":
            print(generateNumbers(1,50,5)+"\t",end="")
            print(generateNumbers(1,12,2))
        case "N":
            novoJogo = True
            print("Ok! :(")
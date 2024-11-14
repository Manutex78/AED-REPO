lotacao = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]

def entradaVeiculo():
    count=0
    for i in range(len(lotacao)):
        for j in range(len(lotacao[i])):
            if lotacao[i][j] == False:
                lotacao[i][j] = True
                print("O seu veiculo está na Fila:", i+1,"Ocupação:", j+1)
                return 

    print("Parque Completo")

def saidaVeiculo(filaVeiculo,ocupacaoVeiculo):
    if lotacao[filaVeiculo][ocupacaoVeiculo] == True:
        lotacao[filaVeiculo][ocupacaoVeiculo] = False
        print("Boa Viagem!")
    else:
        print("Esse lugar não está ocupado! :/")
    
    
def estadoParque():
    ocupados = 0
    livres = 0
    for i in range(len(lotacao)):
        for j in range(len(lotacao[i])):
            if lotacao[i][j] == True:
                ocupados += 1
    livres = 15-ocupados
    print("\nNº de Lugares Ocupados: {:n} \nNº de Lugares Livres: {:n}".format(ocupados,livres))



programa = False
while not programa:
    print("\n\t\tMENU")
    print("1 - Entrada de veículo")
    print("2 - Saída de carro")
    print("3 - Estado do Parque")
    print("0 - Sair")

    try:
        op = int(input("Escolha uma das opções: "))
        if op > 3 or op < 0:
            raise ValueError()
    except ValueError:
        print("Opção Inválida >:/")
    except:
        print("Erro")
    else:
        match op:
            case 1:
                entradaVeiculo()
            case 2:
                filaVeiculo = int(input("Introduza a fila do veiculo: "))-1
    
                ocupacaoVeiculo = int(input("Introduza a ocupação do veiculo: "))-1
                
                saidaVeiculo(filaVeiculo,ocupacaoVeiculo)
            case 3:
                estadoParque()
            case 0:
                programa = True
                print("Adiós! :(")

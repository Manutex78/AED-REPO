lotacao = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]

def entradaVeiculo():
    count=0
    for i in range(len(lotacao)):
        for j in range(len(lotacao[i])):
            if lotacao[i][j] == False:
                lotacao[i][j] = True
                print("O seu veiculo está na Fila:", i+1,"Ocupação:", j+1)
                break
            else:
                count+=1 
        break

    if count == 15:
        print("Parque Completo")

def saidaVeiculo(filaVeiculo,ocupacaoVeiculo):
    lotacao[filaVeiculo],[ocupacaoVeiculo]=False
    
    
def estadoParque():
    ocupados = 0
    livres = 0
    for i in range(len(lotacao)):
        for j in range(len(lotacao[i])):
            ocupados += lotacao.count(True)
    livres = 15-ocupados
    print("Nº de Lugares Ocupados: {:n} \nNº de Lugares Livres: {:n}".format(ocupados,livres))



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
                filaVeiculo = int(input("Introduza a fila do veiculo: "))
                ocupacaoVeiculo = int(input("Introduza a ocupação do veiculo"))
                saidaVeiculo(filaVeiculo,ocupacaoVeiculo)
            case 3:
                estadoParque()
            case 0:
                programa = True
                print("Adiós! :(")

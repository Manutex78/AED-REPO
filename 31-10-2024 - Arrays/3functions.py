meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]


def maiorFaturacao(faturacao):
    maior = max(faturacao)
    pos = faturacao.index(maior)

    return f"O mês de maior faturação foi: {meses[pos]}"

def menorFaturacao(faturacao):
    menor = min(faturacao)
    pos = faturacao.index(menor)

    return f"O mês de menor faturação foi: {meses[pos]}"

def mediaFaturacao(faturacao):
    return f"Média de faturação: {sum(faturacao)/len(faturacao)}"

faturacao = []

for i in range(12):
    try:
        faturacao.append(int(input("Faturação dos mês de {:s} :".format(meses[i]))))
    except:
        print("Valor Inválido")

print(maiorFaturacao(faturacao,meses))
print(menorFaturacao(faturacao,meses))
print(mediaFaturacao(faturacao))
    
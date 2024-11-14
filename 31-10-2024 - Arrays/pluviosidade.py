

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]


def ordenaPluv(pluviosidade):
    pluvio2 = pluviosidade.copy()
    pluvio2.sort(reverse=True)
        
    print("\n\n\nMeses\t\tPluviosidade\n----------------------------")
    for i in range(12):
        pos = pluviosidade.index(pluvio2[i])
        print(meses[pos],"\t\t",pluvio2[i])


pluviosidade = []

for i in range(12):
    try:
        pluviosidade.append(int(input("Pluviosidade no mês de {:s} :".format(meses[i]))))
    except:
        print("Valor Inválido")

ordenaPluv(pluviosidade)

    
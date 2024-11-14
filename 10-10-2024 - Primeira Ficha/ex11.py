idade = int(input("Indique a Idade: "))

#Infância (0 a 12 anos)
if idade >= 0 and idade <=12:

    #Primeira Infância (0 a 2 anos)
    if idade >= 0 and idade <= 2:
        print("Infância - Primeira Infância")
    
    #Infância Intermediária (3 a 6 anos)
    elif idade >= 3 and idade <= 6:
        print("Infância - Infância Intermediária")
    
    #Pré-adolescência (7 a 12 anos)
    elif idade >= 7 and idade <= 12:
        print("Infância - Pré-adolescência")

#Adolescência (13 a 19 anos)
elif idade >= 13 and idade <= 19:

    #Puberdade (13 a 14 anos)
    if idade >= 13 and idade <=14:
        print("Adolescência - Puberdade")
    
    #Adolescência Tardia
    elif idade >=15 and idade <=19:
        print("Adolescência - Adolescência Tardia")

#Adultez
elif idade >= 20 and idade <= 59:

    #Jovem Adulto
    if idade >=20 and idade <= 39:
        print("Adultez - Jovem Adulto")
    
    #Meia-idade
    elif idade >= 40 and idade <= 59:
        print("Adultez - Meia-idade")

#Terceira idade
elif idade >= 60:
    
    #Idosos Jovens
    if idade >= 60 and idade <= 74:
        print("Terceira Idade - Idosos Jovens")

    #idosos velhos
    elif idade >=75:
        print("Terceira Idade - Idosos Velhos")
    


nome = str(input("Nome: "))

print(nome[0:(nome.find(" "))])
print(nome[(nome.rfind(" ")+1):])
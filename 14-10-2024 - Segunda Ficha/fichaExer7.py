numero = int(input("Indique um Número: "))
soma = 0

for i in range (1,numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print("O número é perfeito")
else:
    print("Feio")

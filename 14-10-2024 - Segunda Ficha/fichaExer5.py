
primo = True
num = int(input("Numero: "))
for i in range(2,num):
    if num % i == 0:
        primo = False
        break
if primo == True:
    print ("O número {:n} é primo".format(num))
else:
    print ("O número {:n} não é primo".format(num))
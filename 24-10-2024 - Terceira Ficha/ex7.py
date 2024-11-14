import random

def generatePassword(userName):
    if userName.find(" ") > 0:
        return "Nome inválido"
    else:
        password = ""
        for i in range(0,len(userName)):
            if i % 2 == 0:
                password += userName[i+1]
                password += str(random.randint(1,9))
        password = password + str(len(userName))
        return "password:{:s}".format(password)

userName = input("Nome: ")

print(generatePassword(userName))
        
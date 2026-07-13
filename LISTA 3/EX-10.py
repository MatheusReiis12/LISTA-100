def intervalo():
    x = int(input("Escreva um número inteiro:"))
    x2 = int(input("Escreva outro número inteiro:"))

    for i in range(x,x2+1):
        print(i, end=",")

intervalo()
def soma_entre_numeros():
    x = int(input("INSIRA UM NÚMERO:"))
    x1 = int (input("INSIRA OUTRO NUMERO:"))
    soma = 0

    for i in range (x, x1+1):
        soma += i

    print(soma)

soma_entre_numeros()
def inteiro_ou_decimal():
    x = float(input("Digite um número:"))
    respostas = x % 1

    if respostas > 0 :
        print("Numero decimal")

    else:
        print("Numero Inteiro")

inteiro_ou_decimal()
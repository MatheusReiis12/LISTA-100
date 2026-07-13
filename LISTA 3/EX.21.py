def numero_primo():
    x = int(input("DIGITE UM NUMERO:"))
    if (x % 2 == 1) or (x == 2):
        print("ESSE NUMERO É PRIMO!")

    else:
        print("Esse não é um numero primo!")

numero_primo()
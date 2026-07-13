def segundo_grau():
    
    b=0
    c=0

    a = float(input("Digite um Valor:"))
    if (a == 0):
        pass
    else:
        b = float(input("Digite outro Valor:"))
        c = float(input("Digite o terceiro Valor:"))

    d = (b**2 - 4*a*c)

    if (d < 0):
        print("A equação não existe raizes Reais.")
        pass

    elif (d == 0):
        print("A equação possui apenas uma raiz Real.")

    elif (d > 0):
        print("A equação possui duas raizes Reais!")

segundo_grau()

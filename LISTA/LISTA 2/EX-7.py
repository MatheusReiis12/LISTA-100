def maior_menor():
    X = float (input("Digite o Primeiro Número:"))
    Y = float (input("Digite o Segundo Número:"))
    Z = float (input("Digite o Terceiro Número:"))

    if(X > Y) and (X > Z):
        MI = X

    elif (Y > X) and (Y > Z):
        MI = Y

    elif (Z > X) and (Y > Z):
        MI = Z

    if (Z < X) and (Z < Y):
        MN = Z

    elif (Y < X ) and (Y < Z):
        MN = Y

    elif (X < Y) and (X < Z):
        MN = X

    print(f"O maior Número encontrado é o número {MI} e o menor é {MN}")

maior_menor()

    
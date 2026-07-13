def preço_produtos():
    X = float(input("Digite o preço do Primeiro Produto:"))
    Y = float(input("Digite o preço do Segundo Produto:"))
    Z = float(input("Digite o preço do Terceiro Produto:"))

    if (X < Z) and (X < Y):
        print(f"Compre o Produto de {X}")

    elif (Y < X) and (Y < Z):
        print(f"Compre o Produto com o preço de: {Y}")

    elif (Z < X) and (Z < Y):
        print(f"Compre o Produto com o preço de {Z}")

preço_produtos()
def lado_triangulo():
    X1 =float(input("Digite a medida do primeiro lado:"))
    X2 = float(input("Digite a medida do segundo lado:"))
    X3 = float(input("Digite a medida do terceiro lado:"))

    if (X1 + X2 > X3) or (X2 + X3 > X1) or (X1 + X3 > X2):
        if (X1 == X2 == X3):
            print("Esse é um trinagulo equilatero")

        elif (X1 == X2) or (X1 == X3) or (X2 == X3):
            print("Os lados formam um triangulo Isósceles!")

        else:
            print("Triangulo Escaleno")

    else:
        print("Não existe Triangulo.")


lado_triangulo()

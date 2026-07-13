def qual_operação():
    x = float(input("Digite um Número:"))
    x1 = float(input("Digite outro Número:"))
    operação = input("""
    Qual operação deseja realizar?
        (ESCOLHA O SINAL)
                     
    [*] MULTIPLICAÇÃO
    [/] DIVISÃO
    [+] ADIÇÃO
    [-] SUBTRAÇÃO
    :""")



    if operação == "*":
        multiplicação = x * x1

        if (multiplicação % 2 ) == 0:
            print("Esse numero é par")

        else:
            print("Esse número é impar")

        if multiplicação > 0:
            print("O resultado é positivo")

        else:
            print("O resultado é negativo!")

        if (multiplicação % 1) > 0:
            print("Esse número é decimal")
            
        else: 
            print("Esse número é inteiro!")

        print(f"A multiplicação dos dois numero é {multiplicação}")


    if operação == "/":
        divisão = x / x1

        if (divisão % 2 ) == 0:
            print("Esse numero é par")

        else:
            print("Esse número é impar")

        if divisão > 0:
            print("O resultado é positivo")

        else:
            print("O resultado é negativo!")

        if (divisão % 1) > 0:
            print("Esse número é decimal")
            
        else: 
            print("Esse número é inteiro!")

        print(f"A divisão dos dois numero é {divisão}")


    if operação == "+":
        soma = x + x1

        if (soma % 2 ) == 0:
            print("Esse numero é par")

        else:
            print("Esse número é impar")

        if soma > 0:
            print("O resultado é positivo")

        else:
            print("O resultado é negativo!")

        if (soma % 1) > 0:
            print("Esse número é decimal")
            
        else: 
            print("Esse número é inteiro!")

        print(f"A soma dos dois numero é {soma}")


    if operação == "-":
        subtração = x - x1

        if (subtração % 2 ) == 0:
            print("Esse numero é par")

        else:
            print("Esse número é impar")

        if subtração > 0:
            print("O resultado é positivo")

        else:
            print("O resultado é negativo!")

        if (subtração % 1) > 0:
            print("Esse número é decimal")
            
        else: 
            print("Esse número é inteiro!")

        print(f"A subtração dos dois numero é {subtração}")


    

qual_operação()



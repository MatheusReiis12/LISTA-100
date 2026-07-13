def numeros_entre_0_a_1000():
    lista = []

    while True:

        x = int(input('DIGITE UM NÚMERO:'))
        if (x >= 0) and (x <= 1000):
            lista.append(x)
            xmax = max(lista)
            xmin = min(lista)
            xsoma = xmax + xmin

            print(f"O MAIOR NÚMERO É: {xmax}")
            print(f"O MENOS NÚMERO É: {xmin}")
            print(f"A SOMA DOS MINIMO E DO MÁXIMO É DE {xsoma}")

        else:
            print("NUMERO INCORRETO.")

numeros_entre_0_a_1000()

        

        
def media_aritmética():

    lista = []

    while True:
        x = float(input("DIGITE A NOTA:"))
        lista.append(x)
        total = sum(lista)
        media = total / len(lista)

        print(f"A MÉDIA É: {media:.2f}")



media_aritmética()
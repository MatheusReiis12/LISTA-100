def fibonacci():
    x1 = 0
    x2 = 1
    x3 = 0
    lista = [x1,x2]

    while True:
        x3 = x1 + x2

        x1 = x2
        x2 = x3
        lista.append(x3)



        if x3 > 500:
            print(lista)
            break

fibonacci()
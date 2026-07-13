def focucci ():

    x1 = 1
    x2 = 1
    x3 = 0

    lista = []
    while True:

        x3 = x1+x2


        x1 = x2
        x2 = x3
        
        

        if x3 > 500:
            break

        lista.append(x3)




    print(lista)

focucci()




        

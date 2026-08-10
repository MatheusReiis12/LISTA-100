def numero_primo_divisível():
    lista = []
    x = int(input("DIGITE UM NUMERO:"))


    if (x % 2 == 1) or (x == 2):
        print("ESSE NUMERO É PRIMO!")


    else:
            print("Esse não é um numero primo!")

            for i in range (1,x+1):

                if (x % i == 0):

                    lista.append(i)

            print(f"""
            Esses são os números capazes de dividir o número {x}:
            {lista}""")






numero_primo_divisível()
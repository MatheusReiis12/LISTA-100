def fatorial_limitado():
    while True:
        x = int(input("""
        DIGITE UM NÚMERO:"""))

        if (x < 16) and (x > 0):
            for i in range (1,x):
                x = x * i
                print(x,end=" - ")

        else:
            print("NúMERO INCORRETO")

        if x == 20:
            print("TCHAU")
            break

fatorial_limitado()






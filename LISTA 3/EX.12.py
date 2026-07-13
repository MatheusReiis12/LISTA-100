def gerador_de_tabuada():
    x = int(input("INSIRA UM VALOR NÚMERICO:"))

    print(f"Tabuada do {x}:")

    for i in range (0,11):

        x1 = x * i

        print(f"{x} X {i} = {x1}")



gerador_de_tabuada()


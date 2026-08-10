def fatorial_print():
    lista = []
    x = int(input("DIGITE UM NÚMERO:"))

    for i in range (1,x+1):
        fatorial = x * i
        lista.append(i)

    

    lista.sort(reverse=True)

    print(f"{x}! = ", end="")

    print(*lista, sep=" . " " = ", fatorial)


fatorial_print()
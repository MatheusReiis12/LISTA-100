def min_max_numeros_N ():
    lista = []
    while True:
        x = int(input('DIGITE UM NÚMEROS'))

        lista.append(x)

        xmin = min(lista)
        xmax = max(lista)
        xsoma = xmax + xmin

        print(f'O valor máximo é {xmax}')
        print(f'O valor minimo é {xmin}')
        print(f'A soma dos minimo e máximo é de: {xsoma}')
        

min_max_numeros_N()
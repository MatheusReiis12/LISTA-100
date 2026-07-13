def peça_10_numeros_inteiros():

    pares = []
    impares = []
    for x in range (0, 10):
        x = int(input("DIGITE OS VALORES."))

        if x % 2 == 0:
            pares.append (x)

        else:
            impares.append(x)
            


    print(f"A QUANTIDADE DE NUMEROS PARES É DE:{len(pares)}")
    print(f"A QUANTIDADE DE NÚMEROS IMPARES É DE: {len(impares)}")

peça_10_numeros_inteiros()
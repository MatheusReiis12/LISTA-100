def tabela_panificadora():
    x = float(input("DIGITE O PREÇO DO PÃO:"))

    print("-" * 44)
    print(f"PREÇO DO PÃO: {x}")
    print("PANIFICADORA PÃO DE ONTEM - TABELA DE PREÇOS")
    print("-" * 44)

    for i in range (1,51):

        pão = i * x

        print(f"{i} - R$ {pão:.2f}")



tabela_panificadora()
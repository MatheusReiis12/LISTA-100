def valor_CD():

    coleção = []


    x = int(input("INSIRA O NÚMERO DE CD'S:"))

    for i in range(1,x+1):

        valor_cd = int(input(f"""
        QUAL O VALOR GASTO NO CD {i}
        :"""))
        coleção.append (valor_cd)
        soma = sum(coleção)
        media = soma // x


    print(f"""
    COM O A COLEÇÃO DE {x} CD'S, O SEU GASTO TOTAL FOI DE: {soma}
    E A MÉDIA DE VALOR GASTO PARA CADA CD É: {media}""")









valor_CD()
def votos_candidato():

    candidato1 = 0
    candidato2 = 0
    candidato3 = 0

    while True:
        x = int(input("""
        DIGITE SUA INTENÇÃO DE VOTO!
        [1] CANDIDATO 1
        [2] CANDIDATO 2
        [3] CANDIDATO 3
        :"""))


        if (x == 1):
            candidato1 += 1

        elif (x == 2):
            candidato2 += 1

        elif (x == 3):
            candidato3 += 1

        else:
            print("""
        VOTO INVÁLIDO.""")


        print(f"""
---------------------------------------------------------------
        INTENÇÕES DE VOTOS!
        CANDIDATO 1: {candidato1}
        CANDIDATO 2: {candidato2}
        CANDIDATO 3: {candidato3}
---------------------------------------------------------------""")


votos_candidato()
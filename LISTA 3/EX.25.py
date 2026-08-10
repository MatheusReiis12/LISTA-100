def pessoa_idade():

    turma = []

    while True:
        x = int(input("DIGITE A SUA IDADE:"))
        turma.append(x)
        soma = sum(turma)
        media = soma / len(turma)

        if (media >= 0) and (media <= 25):
            print(f"""
A IDADE DA TURMA ANDA VARIANDO ENTRE 0 E 25!
MÉDIA: {media:.2f}""")

        elif (media >= 26) and (media <= 60):
            print(f"""
            A MÉDIA DA TURMA VARIA ENTRE 26 E 60
            MÉDIA: {media:.2f} """)


        elif (media > 60):
            print(f"""
            A MÉDIA DA TURMA JA PASSOU DE 60 ANOS!
            MEDIA: {media:.2f}""")

pessoa_idade()
            
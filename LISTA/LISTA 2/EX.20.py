def nota_parcial_aluno():
    nota1 = float(input("Digite a sua primeira nota:"))
    nota2 = float(input("Digite a sua segunda nota:"))
    nota3 = float(input("Digite a sua terceira nota:"))

    media = (nota1+nota2+nota3) / 3

    if (media >= 7):
        print("PARABÊNS, VOCE FOI APROVADO!")

    if (media < 7):
        print("infelizmente, voce foi reprovado... ;-;")

    if (media == 10):
        print("PARABÊNS, VOCÊ FOI APROVADO COM DISTINÇÃO!")

nota_parcial_aluno()
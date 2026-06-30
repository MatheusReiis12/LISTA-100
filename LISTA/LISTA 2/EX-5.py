X = float(input("Digite a primeira nota:"))
Y = float(input("Digite a Segunda nota do Aluno:"))
Z = (X+Y) / 2 


def media_notas():
    if (Z == 10):
        print(f"""PARABÊNS VOCÊ FOI APROVADO COM DISTINÇÃO!!! :D
          A sua média foi de {Z}""")

    elif (Z >= 7):
        print(f"""Parabêns você foi aprovado!! 
          A sua média foi de {Z}""")

    elif (Z < 7):
        print(f"""Infelizmente, você foi reprovado :/ 
          A sua média foi de {Z}""")
        
media_notas()


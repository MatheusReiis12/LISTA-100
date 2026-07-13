def ler_numeros():
    print("""O jogo começa AGORA!
Me diga 3 Números, e irei adivinhar qual é o maior deles!
Está PRONTO?""")
    
    X = float(input("""SENDO ASSIM, escreva o primerio Número!:
R:"""))
    Y = float(input("""Escreva o Segundo Número! Não tente me enrolar... :p
R:"""))
    Z = float(input("""Agora para o Grande finale... ESCREVA O TERCEIRO E ULTIMO NÚMERO!:
R:"""))
    
    if (X > Y) and (X > Z):
        print(f"""Estou vendo Aqui... Estou Presentindo... O MAIOR NÚMERO DIGITADO FOI..." 
        "O NÚMERO {X}!!""")

    elif (Y > X) and (Y > Z):
        print(f"""Estou vendo Aqui... Estou Presentindo que... O MAIOR NÚMERO DIGITADO FOI...!!!!!!!!!!!! 
              O NÚMERO {Y}!!""")

    elif (Z > X) and (Z > Y):
        print(f"""Estou vendo Aqui... Estou Presentindo que... O MAIOR NÚMERO DIGITADO FOI...!!!!!!!!!!!!" 
        "O NÚMERO {Z}!!""")

ler_numeros()
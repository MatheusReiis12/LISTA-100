def lendo_notas():
    nota = float(input("Digite a sua primeira nota do semestre:"))
    nota1 = float(input("Digite a sua segunda nota do semestre: "))
    media = (nota+nota1) / 2

    print("""
          - MÉDIA DE APROVEITAMENTO -     -- CONCEITOS --
          - Entre 9.0 a 10.0                     (A)
          - Entre 7.5 e 9.0                      (B)
          - Entre 6.0 e 7.5                      (C)
          - Entre 4.0 e 6.0                      (D) 
          - Entre 4.0 e zero                     (E)""")

    if (media >= 9.0) and (media <= 10.0):
        print(f""" 
            SUA NOTA INICIAL FOI DE: {nota}
            SUA SEGUNDA NOTA FOI DE: {nota1}
            PARABÊNS!! A sua média parcial é de {media}. Você foi incrivel!  
            VOCE TIROU (A)""")

    elif (media >= 7.5)  and (media < 9.0):
        print(f"""
              - Sua nota inicial foi de: {nota}
              - Sua segunda nota foi de: {nota1}
              - PARABÉNS, VOCE TIROU NOTA: {media} um lindo (B)""")

    elif (media >= 6.0) and (media < 7.5):
        print(f"""
              - Sua nota inicial foi de: {nota}
              - Sua segunda nota foi de: {nota1}
              - PARABENS VOCE TIROU NOTA: {media} um lindo (C)""")

    elif (media >= 4.0) and (media < 6.0):
        print(f"""
            - Sua nota Inicial foi de: {nota}
            - Sua segunda nota foi de: {nota1}
            - Isso não é bom... Voce tirou nota {media} (D)"   
            - Voce é melhor do isso Buddy!""")
        
    elif (media >= 0.0) and (media < 4.0):
        print(f""" 
            - Infelizmente, voce não conseguiu uma boa nota dessa vez... Mas vai dar tudo certo! 
            - Sua nota Inicial = {nota}
            - Sua Segunda nota Foi {nota1}
            - Sua nota media final é: {media} um pequeno (E)""")


lendo_notas ()
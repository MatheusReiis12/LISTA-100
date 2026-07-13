def taxa_de_crescimento_input():
    populacao = float(input("População Atual:"))
    taxa_de_crescimento = float(input("Digite a taxa de crescimento inicial:"))
    anos = int(input("Voce quer saber o crescimento, em uma estimativa de quantos anos?" \
    ""))
    taxa_de_crescimento1 = 1 + (taxa_de_crescimento / 100)
    x = populacao 
    i= 0




    if (populacao >= 1):
        if (taxa_de_crescimento >= 1) and (taxa_de_crescimento <= 100):

            while i < anos:

                x = x * taxa_de_crescimento1 # CONTA PARA SABER A TAXA DE POPULAÇÃO
                i += 1

                if i == anos:
                    print(f"""O crescimento dessa população será de: {x:.2f}
                          Depois de: {anos} Anos!""")
                    break

taxa_de_crescimento_input()


def caixa_eletronico():
    x = int(input("Digite o valor de saque:"))
    a = 0
    b = 0 
    c = 0
    d = 0
    e = 0

    if (x > 10) and (x < 600):

        #NOTA DE 100
        if (x >= 100):
            a = (x // 100)
            b = (x % 100)

            # NOTA DE 50
            if (b < 100) or (b == 50):
                b = b // 50
                c = ((x % 100) % 50)
                


                if (c < 50):
                    c = c // 10 #NOTAS
                    d = (((x % 100) % 50) % 10) #RESTO


                    if (d < 10):
                        d = d // 5
                        e = ((((x % 100) % 50) % 10) % 5)

                        if (e < 5):
                            e = e // 1


    print(f"VOCE RECEBERA {a} notas de 100, {b} notas de 50, {c} notas de 10 {d}, notas de 5, {e} moedas de 1 real")
                    
                    

caixa_eletronico()
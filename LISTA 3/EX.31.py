def máquininha_cartão():

    i= 0
    lista = []
    while True:

            i += 1
            x = float(input(f"Produto {i}:"))
            lista.append(x) 
            soma = sum(lista)



            if x == 0:

                print(f"TOTAL: {soma}")
                y = float(input("Dinheiro:"))
                troco = y - soma

                print(f"""
                Total: {soma} 
                Dinheiro: {y}
                Troco: {troco}""")



                

    



máquininha_cartão()
# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#  Até 5 Kg Acima de 5 Kg
# File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
# Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
# Picanha R$ 6,90 por Kg R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão 
# Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
#  tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.



#  Até 5 Kg  // Acima de 5 Kg

# File Duplo R$ 4,90 por Kg / R$ 5,80 por Kg
# Alcatra R$ 5,90 por Kg /  R$ 6,80 por Kg/;
# Picanha R$ 6,90 por Kg / R$ 7,80 por Kg

def açougue():

    valor = float()
    valor_total = float()
    valor_d = float()
    x = input("""
    Qual carne voce deseja?" 
    [File Duplo] 
    [Alcatra] 
    [Picanha]""")

    x1 = float(input("""Quantos Kilos de Carne deseja?
                     """))

    x2 = input("Será usado o cartão tabajara como forma de pagamento?")

    x = x.upper()
    x2 = x2.upper()


    if x2 == "SIM":
        t = "Cartão Tabajara"

    else:
        t = "Sem cartão Tabajara"


    if x == "PICANHA":
        if x1 < 5:
            picanha = (x1 * 6.90)
            valor_total = picanha

            if x2 == "SIM" or x2 == "S":
                valor_d = (picanha * 0.05)
                valor = picanha - (picanha * 0.05)

            else:
                valor = picanha



        if x1 >= 5:
            picanha = x1* 7.80
            valor_total = picanha

            if x2 == "SIM" or x2 == "S":
                valor_d = (picanha * 0.05)
                valor = picanha - (picanha * 0.05)

            else:
                valor = picanha

    if x == "FILE DUPLO":
        if x1 < 5:
            file_duplo = x1 * 4.90
            valor_total = file_duplo

            if x2 == "SIM" or x2 == "S":
                valor_d = (file_duplo * 0.05)
                valor = file_duplo - (file_duplo * 0.05)

            else:
                valor = file_duplo




        if x1 >= 5:
            file_duplo = x1* 5.80
            valor_total = file_duplo

            if x2 == "SIM" or x2 == "S":
                valor_d = (file_duplo * 0.05)
                valor = file_duplo - (file_duplo * 0.05)

            else:
                valor = file_duplo


    if x == "ALCATRA":
        if x1 < 5:
            Alcatra = x1 * 5.90
            valor_total = Alcatra


            if x2 == "SIM" or x2 == "S":
                valor_d = (Alcatra * 0.05)
                valor = Alcatra - (Alcatra * 0.05)


            else:
                valor = Alcatra



        if x1 >= 5:
            Alcatra = x1* 6.80
            valor_total = Alcatra

            if x2 == "SIM" or x2 == "S":
                valor_d = (Alcatra * 0.05)
                valor = Alcatra - (Alcatra * 0.05)


            else:
                valor = Alcatra
            


    print(f"""
---- NOTA FISCAL ----
Tipo: {x}
Quantidade: {x1:.2f} Kg
Preço Total: R$ {valor_total:.2f}
Tipo de Pagamento: {t}
Valor do Desconto: R$ {valor_d:.2f}
Valor a Pagar: R$ {valor:.2f}
""")
        

        

        #contendo as informações da compra:
        #tipo e quantidade de carne, 
        # preço total, 
        # tipo de pagamento, 
        # valor do desconto e 
        # valor a pagar.





açougue()
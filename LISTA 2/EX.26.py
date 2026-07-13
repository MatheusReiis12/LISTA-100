# #26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
# preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


#gasolina: até 20 litros = 4%
            #depois de 20 litros  = 6%
            #preço: 2.50

#alcool : até 20 litros = 3%
        # Acima de 20 litros, desconto de 5%


def descontos_comb():
    x = float(input("Digite quantos litros de combustível deseja:"))

    x1 = input("""
               Qual o tipo de Combustível?
                [G] Gasolina 
                [A] Álcool
               """)
    
    x1 = x1.upper() # NÃO ESQUECER DO PARENTESES!


    #PREÇO DO ALCOOL
    if (x1 == "A") or (x1 == "ÁLCOOL") or  (x1 == "ALCOOL"):
        if x <= 20:
            x = (x * 1.90) - (x * 0.3)
            print(f"O valor que deverá ser pago é de: {x}")
        
        if x >= 20:
            x = (x*1.90) - (x * 0.4)
            print(f"O valor que deverá ser pago é de: {x}")
        
    
    


    elif (x1 == "G") or (x1 == "GASOLINA"):
        if x <= 20:
            x = (x* 2.50) - (x*0.4)

            print(f"O valor que deverá ser pago é de: {x}")

        if x >= 20:
            x = (x*2.50) - (x*0.6)

            print(f"O valor que deverá ser pago é de: {x}")





descontos_comb()
def numeros_ordem_crescente():
    X = float(input("Digite um Número:"))
    Y = float(input("Digite outro Número:"))
    Z = float(input("Digite o Terceiro Número:"))


#NÚMERO MAIOR
    if (X > Y) and (X > Z):
        xmaior = X
    elif (Y > X) and (Y > Z):
        xmaior = Y
    elif (Z > X) and (Z > Y):
        xmaior = Z
    

#NÚMERO MENOR
    if (X < Y) and (X < Z):
        xmenor = X
    elif (Y < X) and (Y < Z):
        xmenor = Y
    elif (Z < X) and (Z < Y):
        xmenor = Z


 #NÚMERO DO MEIO
    if (X < Y) and (X > Z) or (X > Y) and (X < Z) :
        xmeio = X
    elif (Y < X) and (Y > Z) or (Y > X) and (Y < Z):
        xmeio = Y
    elif (Z < Y) and (Z > X) or (Z > X) and (Z < Y):
        xmeio = Z

    print(f"""
O maior número é: {xmaior}
E o número do meio é: {xmeio}
O menor número é: {xmenor}

""")
    
numeros_ordem_crescente()
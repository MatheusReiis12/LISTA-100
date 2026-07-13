def corrigindo_datas():
    print("DIGITE UMA DATA!")

    meses = 0
    dia = int(input("Digite um dia"))
    meses = int (input("Digite um mês"))
    ano = int (input("Digite um ano:"))

    #separar mes que tem 31dias e mes que tem 30 dias e mes que tem 28 ou 29 dias
    if (ano >= 1) and (ano <= 2026):
        if (meses == 1) or (meses == 3) or (meses == 5) or (meses == 8) or (meses == 10) or (meses == 12):
            if (dia <= 31) and (dia >= 1):
                print(f"{dia}/{meses}/{ano}")

    if (ano >= 1) and (ano <= 2026):
        if (meses == 4) or (meses == 6) or (meses == 9) or (meses == 11):
            if (dia <= 30) and (dia >= 1):
                print(f"{dia}/{meses}/{ano}")
            

    if (ano >= 1) and (ano <= 2026):
        if (meses == 2): 
            if (dia < 29) and (dia > 1):
                print(f"{dia}/{meses}/{ano}")

    if ((ano // 4) == 0 ):
        print("Esse ano é Bissexto!")
        if (meses == 2): 
            if (dia <= 28) and (dia >= 1):
                print(f"{dia}/{meses}/{ano}")

    else: 
        print("Data inválida")
    

    

    

corrigindo_datas()


#dia 30: 
    


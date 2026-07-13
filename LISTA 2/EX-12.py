#Descontos : IMPOSTO DE RENDA = VARIÁVEL CONFORME O SALÁRIO // 3% SINDICATO // FGTS 11% DO SALÁRIO BRUTO (mas não é descontado) 
#Salário liquido =  Salário bruto - Descontos (IR E SINDICATO)
#VALOR DE HORA E HORAS TRABALHADAS

def folha_de_pagamento ():
    #Calculo de horas 

    i = 0
    ir = 0
    inss = 0
    fgts = 0
    Salario_liquido = 0
    Total_de_descontos = 0

    X = float(input("Digite o valor da sua hora:"))
    H = float(input("Digite suas horas trabalhadas"))
    
    #Salário Bruto
    XH = (X*H)

    #Salário até 900 = Isento do desconto do IR
    if (XH <= 900):
        Sindicato = (XH * 0.03)
        fgts = (XH * 0.11)
        inss = (XH* 0.10)
        Total_de_descontos = (ir+Sindicato+inss)
        Salario_liquido = (XH - Total_de_descontos)


    #Salário até 1500 = 5% do desconto do IR 3% DO SINDICATO e 11% a mais do fgts
    elif (XH > 900) and (XH <= 1500):
        i = 0.05
        ir = (XH*0.05)
        inss = (XH* 0.10)
        Sindicato = (XH * 0.03)
        fgts = (XH * 0.11)
        Total_de_descontos = (ir+Sindicato+inss)
        Salario_liquido = (XH - Total_de_descontos)


    #Salário até 2500 = 10% do desconto do ir 3% DO SINDICATO e 11% a mais do fgts
    elif (XH > 1500) and (XH <= 2500):
        i = 0.10
        ir = (XH*0.10)
        inss = (XH* 0.10)
        Sindicato = (XH * 0.03)
        fgts = (XH * 0.11)
        Total_de_descontos = (ir+Sindicato+inss)
        Salario_liquido = (XH - Total_de_descontos)

    #Salário acima de 2500 = 20% do desconto do ir 3% DO SINDICATO e 11% a mais do fgts
    elif (XH > 2500):
        i = 0.20
        ir = (XH*0.20)
        inss = (XH* 0.10)
        Sindicato = (XH * 0.03)
        fgts = (XH * 0.11)
        Total_de_descontos = (ir+Sindicato+inss)
        Salario_liquido = (XH - Total_de_descontos)


    print(f"""------------------------ Folha de Pagamento ------------------------

Salário Bruto: ({X} * {H})  : {XH}

(-) IR {i}                      :{ir}

(-) INSS 10%                  :{inss}

FGTS (11%)                    :{fgts}

Total de Descontos            :{Total_de_descontos}

Salário Liquído               :{Salario_liquido}""")

folha_de_pagamento()
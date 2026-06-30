def salario_colaboradorador():
    X = float(input("Digite o seu Salário:"))

    #Salários até R$ 280,00 (incluindo) : aumento de 20%
    
    if (X <= 280):
        b = (X*1.20)
        c = (X*0.20)
        print(f"""Salário antes do reajuste:{X}
o percentual de aumento aplicado: 15%
o valor do aumento: {c}
o novo salário, após o aumento:{b}
 """)
        
#Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

    elif (X > 280) and (X <= 700):
        b = (X*1.15)
        c = (X*0.15)
        print(f"""Salário antes do reajuste:{X}
o percentual de aumento aplicado: 15%
o valor do aumento: {c}
o novo salário, após o aumento:{b}
 """)

#Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

    elif (X > 700) and (X < 1500):
        b = (X*1.10)
        c = (X*0.10)
        print(f"""Salário antes do reajuste:{X}
o percentual de aumento aplicado: 10%
o valor do aumento: {c}
o novo salário, após o aumento:{b}
 """)
    
#Salários de R$ 1500,00 em diante : aumento de 5%
    elif (X >= 1500):
        b = (X * 1.05)
        c = (X*0.10)
        print(f"""Salário antes do reajuste:{X}
o percentual de aumento aplicado: 5%
o valor do aumento: {c}
o novo salário, após o aumento:{b}
 """)
        
salario_colaboradorador()

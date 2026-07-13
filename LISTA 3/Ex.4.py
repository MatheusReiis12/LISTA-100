#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#8000 + 0.3%
#população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%
#200000 1.5%

def taxa_de_crescimento():

    contador = 0

    a2 = 80000
    b2 = 200000
    b1 = b2 * 1.015
    a1 =  a2 * 1.03






    while True:
        if (a1 < b1 ):
                
                a1 =  a1 * 1.03
                b1 = b1 * 1.015
                

                print(f"""
                      População A: {a1}
                      População B: {b1}""")
                contador = contador + 1

        if (a1 > b1):
             print(f"""A população do país A ultrapassou a do país B depois de {contador} ANOS! 
                   O País A tem {a1} habitantes
                   E o País B tem {b1}""")
             break
             
print("OI")

taxa_de_crescimento()
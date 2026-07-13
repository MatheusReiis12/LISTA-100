def turno_estuda():
    X = input("""-------- DIGITE QUAL TURNO VOCÊ ESTUDA --------
[M] MATUTINO
[V] VESPERTINO
[N] NOTURNO
R:""")
    
    X1 = X.upper()
    
    if (X1 == "M") or (X1 == "MATUTINO"):
        print("BOM DIA!")
    
    elif (X1 == "V") or (X1 == "VESPERTINO"):
        print("BOA TARDE!")

    elif (X1 == "N") or (X1 == "NOTURNO"):
        print("BOA NOITE!")

turno_estuda()
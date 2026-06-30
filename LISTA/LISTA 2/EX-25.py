def crime_vitima():
    a1 = input("Telefonou para a vitima? [S/N]")
    a2 = input("Esteve no local do crime? [S/N]")
    a3 = input("Mora perto da vitima? [S/N]")
    a4 = input("Devia para a vitima? [S/N]")
    a5 = input("Já trabalho para a vitima? [S/N]")

    a1 = a1.upper
    a2 = a2.upper
    a3 = a3.upper
    a4 = a4.upper
    a5 = a5.upper
    

    contador = 0
    não_contado = 0

    if a1 == "S":
        contador = contador + 1

    if a2 == "S":
        contador = contador + 1
    
    if a3 == "S":
        contador = contador + 1

    if a4 == "S":
        contador = contador + 1

    if a5 == "S":
        contador = contador + 1

    if a1 == "N":
        não_contado = não_contado + 1

    if a2 == "N":
        não_contado = não_contado + 1

    if a3 == "N":
        não_contado = não_contado + 1

    if a4 == "N":
        não_contado = não_contado + 1

    if a5 == "N":
        não_contado = não_contado + 1


    if contador == 2:
        print("Voce é suspeita...")

    if (contador == 3) or (contador == 4):
        print("Um pouco suspeito...")

    if (contador == 5):
        print("ASSASSINO!")

    
        
crime_vitima()
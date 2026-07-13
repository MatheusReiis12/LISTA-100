def ano_bissexto ():
    X = int(input("""
----- DIGITE UM ANO -----
: """))
    if ((X // 400) == 0) or ((X // 4) == 0):
        print("Esse ano, é um ano Bissexto!")

    else:
        print("Esse ano não é bissexto.")

ano_bissexto()

    
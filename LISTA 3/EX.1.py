i = 0

while True:
        i = int(input("""Digite uma nota de 0 a 10
                      R: """))
        print(i)

        if (i > 10) or (i < 0):
                print("insira um novo valor!")

        elif (i <= 10) and (i >= 1):
                print("Voce digitou um valor válido")
                break
        

def dias_da_semana():
    dias = int(input("""
-------------------- DIGITE UM NÚMERO DE 1 a 7 --------------------
                     1 - Segunda-Feira
                     2 - Terça-Feira
                     3 - Quarta-Feira
                     4 - Quinta-Feira
                     5 - Sexta-Feira
                     6 - Sábado
                     7 - Domingo
                     Resposta:"""))

    if (dias == 1) :
        print("Segunda-feira! Agora Fedeu!")

    if (dias == 2):
        print("Terça-Feira! Vamo lá, falta algumas horas para Quarta!")

    if (dias == 3):
        print("Quarta-Feira! Bora, Bora! Meio da semana já!")

    if (dias == 4):
        print("Quinta-Feira! 1 DIA ANTES DE SEXTA, REPITO, 1 DIA ANTES DA SEXTA!")

    if (dias == 5):
        print("Sexta-Feira! DIA INTERNACIONAL PARA BEBER TODAS! TODAAAAAAAAAAAAS!")

    if (dias == 6):
        print("Sabado! Sabadinho, pézinho no chão.Tranquilidade máxima!")

    if(dias == 7):
        print("Domingo! O fatidico... Domingo a noite. O cruel DOMINGO A NOITE!")


dias_da_semana()
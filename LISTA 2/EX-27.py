#    Até 5 Kg                     Acima de 5 Kg
#Morango R$ 2,50 por Kg           R$ 2,20 por Kg
#Maçã    R$ 1,80 por Kg           R$ 1,50 por Kg


#Mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00 = 10% de desconto
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
#maças adquiridas e escreva o valor a ser pago pelo cliente.

def preço_frutas():
    morango = 0
    maça = 0
    preço_totald = 0

    x = float(input("Quantos Kilos de morango deseja?"))
    x1 = float(input("""
Quantos kilos de maçã desejas?" 
    """))


    if (x > 5):
        morango = x * 2.20 #preço com mais de 5 kg
        print(f"O preço da maça é de 2,20. O preço a ser pago é de {morango:.2f}")
    if (x < 5):
        morango = x * 2.50 # preço com menos de 5kg
        print(f"O preço da maça é de 2,50. O preço a ser pago é de {morango:.2f}")

    if (x1 > 5):
        maça = x1 * 1.50 #preço com mais de 5 kg
        print(f"O preço da maça é de 1.50. o preço a ser pago é de {maça:.2f}")

    if (x1 < 5):
        maça = x1 * 1.80 # preço com menos de 5kg
        print(f"O preço da maça é de 1.80. o preço a ser pago é de {maça:.2f}")

    preço_total = morango+maça

    if ((x1 + x) > 8) or (maça + morango > 25):
        preço_totald = (maça + morango) - ((maça + morango)* 0.10)
        print(f"O preço total a ser pago é de {preço_totald:.2f}")

    else:
        print(f"O preço total a ser pago é de: {preço_total:.2f}")

preço_frutas()


    







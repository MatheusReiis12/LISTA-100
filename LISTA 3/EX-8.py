def ler_numeros ():
    x = float(input("Digite um número:"))
    x1 = float(input("Digite um número:"))
    x2 = float(input("Digite um número:"))
    x3 = float(input("Digite um número:"))
    x4 = float(input("Digite um número:"))

    soma = 0

    xlista = [x,x1,x2,x3,x4]

    for i in xlista:
        soma += i #Vai ser somado! soma + i (Valor dos valores em cada posição na lista.)

    media = soma / len(xlista)

    print(f"""
        A média dos valores é de{media}
        A soma de todos eles é de {soma}""")




ler_numeros()
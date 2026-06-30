#x = int(input("Digite um número"))


# unidade = x % 1

# print(unidade)

def ler_numero():
    x = int(input("Insira um número:"))
    if (x < 1000):
        a = x // 100
        b = (x % 100) // 10
        c = ((x % 100) % 10) // 1

        print(f"{a} centenas, {b} dezenas e {c} unidades")

ler_numero() 
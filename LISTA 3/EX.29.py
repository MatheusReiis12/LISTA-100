#ARTIGOS DE 1.99 = 10 CAIXAS

def tabela_de_preços():
    x = 0
    print("LOJAS QUASE DOIS - TABELA DE PREÇOS")
    print(f"{'PRODUTOS':<10} | {'PREÇO':<10}")
    print("-" * 23)

    for i in range (1,51):
        x = 1.99 * i

        print(f"{i} - R$ {x}")

tabela_de_preços()
        

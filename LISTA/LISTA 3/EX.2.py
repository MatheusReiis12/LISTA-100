def ler_nome_de_usuário():
    
    while True:
        usuario = input("""
            Digite o Seu nome de Usuário
            :""")
        senha = input("""
                      Digite sua Senha
                      :""")
        
        if usuario == senha:
            print("""
                  --- Tem algo errado :( 
                Sua senha está igual ao nome de usuário
                Digite Novamente ---""")
            
        elif usuario != senha:
            print("Logando...")
            break
        
ler_nome_de_usuário()
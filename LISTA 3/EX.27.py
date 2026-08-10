def alunos_turma():
    numeros_de_alunos = []
    x = int(input("DIGITE O NUMERO DE TURMAS:"))

    for i in range (1,x+1):
        x1 = int(input(f"DIGITE O NÚMERO DE ALUNOS DA TURMA {i}:"))

        if (x1 <= 40):
            numeros_de_alunos.append(x1)

        else:
            print("NÚMERO INVÁLIDO")



    soma = sum(numeros_de_alunos)
    media = soma // x

    print(f"""
    O NÚMERO DE TURMAS É DE: {x}
    O NÚMERO TOTAL DE ALUNO É DE: {soma}
    EM MÉDIA, FICARÁ {media} EM CADA SALA.""")


       



alunos_turma()
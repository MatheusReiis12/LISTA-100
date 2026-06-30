
def validacao():

    while True:

        nome= input("Digite seu Nome")

        if len(nome) > 3:
            print("Nome válido")
            idade= int(input("Digite seu idade"))

            if (idade > 0) and (idade < 150):
                print("Idade Válida")
                salario= float(input("Digite seu Salário"))

                if (salario > 0):
                    print(f"Salário de: {salario} Valido")
                    sexo= input("Digite seu sexo [F] Feminino ou [M] Masculino")
                    sexo = sexo.upper()
                    
                    if (sexo == "F") or (sexo == "M"):
                        print("Sexo Válido")
                        estado_civil= input("Qual seu estado Cívil? [S] Solteiro / [C] Casado / [V] Viuvo / [D] Divorciado")
                        estado_civil = estado_civil.upper()

                        if (estado_civil == "S") or (estado_civil == "C") or (estado_civil == "V") or (estado_civil == "D"):
                            print("Estado Cívil Válido")
                            print("Validação realizada com Sucesso!")
                            break
                            


                            
                        else:
                            print("Estado Cívil Inválido")

                    else:
                        print("Sexo Inválido")
                        
                else:
                        print("Salário inválido")


            else:
                    print("Idade Inválida")

        else:
            print("Nome Inválido")


validacao()
nota_registrada = None
faltas_registradas = None

while True:
    print("========= SISTEMA DE NOTAS =========")
    print("1 - Informar nota")
    print("2 - Informar faltas")
    print("3 - Consultar situação do aluno")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nota = float(input("Digite a nota do aluno: "))

        if nota >= 0 and nota <= 10:
            nota_registrada = nota
            print("Nota registrada com sucesso.")
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

    elif opcao == "2":
        faltas = int(input("Digite o número de faltas do aluno: "))

        if faltas >= 0:
            faltas_registradas = faltas
            print("Faltas registradas com sucesso.")
        else:
            print("Número de faltas inválido.")

    elif opcao == "3":
        if nota_registrada is None:
            print("Nenhuma nota foi registrada ainda.")
        elif faltas_registradas is None:
            print("Nenhuma falta foi registrada ainda.")
        else:
            print("Nota:", nota_registrada)
            print("Faltas:", faltas_registradas)

            if faltas_registradas > 4:
                situacao = "Reprovado por faltas"
            elif nota_registrada >= 7:
                situacao = "Aprovado"
            elif nota_registrada >= 3:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print("Situação:", situacao)

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")

# Adicionar o numero de faltas do aluno e nao pode ser > 4 se for maior - reprovado direto
#  
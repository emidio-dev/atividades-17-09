saldo = 2000.00

while True:
    print("CAIXA ELETRÔNICO")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Saldo atual: R$", saldo)

    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo = saldo + valor
            print("Depósito realizado com sucesso.")
            print("Saldo atual: R$", saldo)
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")

    elif opcao == "3":
        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Valor inválido. O saque deve ser maior que zero.")
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldo = saldo - valor
            print("Saque realizado com sucesso.")
            print("Saldo atual: R$", saldo)

    elif opcao == "4":
        print("Encerrando o caixa eletrônico...")
        break

    else:
        print("Opção inválida.")

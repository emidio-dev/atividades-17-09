def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return a / b


while True:
    print("CALCULADORA")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    if opcao in ("1", "2", "3", "4"):
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = somar(numero1, numero2)
        elif opcao == "2":
            resultado = subtrair(numero1, numero2)
        elif opcao == "3":
            resultado = multiplicar(numero1, numero2)
        elif opcao == "4":
            resultado = dividir(numero1, numero2)

        if resultado is not None:
            print("Resultado:", resultado)
    else:
        print("Opção inválida. Tente novamente.")

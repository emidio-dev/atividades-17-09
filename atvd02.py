votos_cebolinha = 0
votos_gohan = 0
votos_athena = 0

while True:
    print("========= VOTAÇÃO =========")
    print("1 - Cebolinha")
    print("2 - Gohan")
    print("3 - Athena")
    print("4 - Encerrar votação")

    voto = input("Digite seu voto: ")

    if voto == "1":
        votos_cebolinha = votos_cebolinha + 1
        print("Voto registrado para o Cebolinha.")
    elif voto == "2":
        votos_gohan = votos_gohan + 1
        print("Voto registrado para o Gohan.")
    elif voto == "3":
        votos_athena = votos_athena + 1
        print("Voto registrado para a Athena.")
    elif voto == "4":
        break
    else:
        print("Opção inválida.")

total_votos = votos_cebolinha + votos_gohan + votos_athena

print("========= RESULTADO =========")
print("Candidato Cebolinha:", votos_cebolinha, "votos")
print("Candidato Gohan:", votos_gohan, "votos")
print("Candidata Athena:", votos_athena, "votos")
print("Total de votos:", total_votos)

if total_votos > 0:
    media_votos = total_votos / 3
    print("Média de votos por candidato:", media_votos)

    if votos_cebolinha > votos_gohan and votos_cebolinha > votos_athena:
        print("Vencedor: Cebolinha")
    elif votos_gohan > votos_cebolinha and votos_gohan > votos_athena:
        print("Vencedor: Gohan")
    elif votos_athena > votos_cebolinha and votos_athena > votos_gohan:
        print("Vencedora: Athena")
    else:
        print("Resultado: houve empate entre os candidatos mais votados.")
else:
    print("Nenhum voto foi registrado.")

#adicionar o total de votos  + media de votos
# mostrar quem foi o ganhador
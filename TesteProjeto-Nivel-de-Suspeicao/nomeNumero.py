def nomeNumero():  # Aqui criar uma lista com os nomes ligados ao seu respectivo número.

    for linha in agenda:
        if linha != "agenda" and linha != "chamadas":
            pedacos = linha.split(":")
            #print(pedacos)
            dadosDono = str(pedacos[0]).split("-")
            nomes.append(dadosDono[0])
            numeros.append(dadosDono[1])

        if linha == "chamadas":
            break

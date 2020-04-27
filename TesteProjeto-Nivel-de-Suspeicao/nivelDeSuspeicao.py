def niveldeSuspeicao(numero_de_chamadas):
    lista_de_chamadas = criarListaChamadas()
    print('Lista de reciprocidade de chamadas desejadas:')
    print('----------------------------------------------')
    for i, e in enumerate(numeros):
        for x in range(len(numeros)):
            if (chamadas[x]).count(e) >= numero_de_chamadas:
                print('%s <-> %s (Nível alto de suspeicao)'% (nomes[i], nomes[x]))
                break
        else:
            print(('%s <-> %s '% (nomes[i], nomes[x])))
            break

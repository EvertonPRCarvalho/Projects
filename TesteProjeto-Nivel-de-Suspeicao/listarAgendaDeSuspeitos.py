def listarAgendaDeSuspeitos(listaNmes, listaNumeros):

    lista = []

    for i, e in enumerate(listaAgenda):

        if e != ['agenda'] and e != ['chamadas']:
            lista.append(e)

            for cont in e:
                separa = cont.split(':')
                x = separa[0].split('-')
                nomes.append(x[0])
                numeros.append(x[1])
                print(x)

        if e == ['chamadas']:
            break
        if e in numeros:
            print(e)

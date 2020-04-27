def contatosEmAgenda():
    #lista = passar_por_nomes()
    for e in range(len(lista)):
        for i in range(len(nomes)):
            if nomes[e] in lista[i] and nomes[i] in lista[e]:
                break
        print('%s <-> %s'% (nomes[e],nomes[i]))
